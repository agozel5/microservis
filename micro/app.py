from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Oturum yönetimi için gereklidir.

# Absolute path for the SQLite database file
db_path = os.path.join(os.getcwd(), 'users.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'  # Veritabanı bağlantısı
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Deprecation warning
db = SQLAlchemy(app)


# Kullanıcı modeli
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


# Veritabanını başlat (ilk kez çalıştırıldığında)
def create_tables():
    try:
        with app.app_context():
            if not os.path.exists(db_path):  # Check if the database file exists
                db.create_all()  # Create tables if the database doesn't exist
                print("Database created and tables created successfully.")
            else:
                print("Database already exists.")
    except Exception as e:
        print(f"Error while creating tables: {e}")


# Anasayfa route'u
@app.route('/')
def home():
    if 'user_id' in session:
        username = session['username']
        return render_template('index.html', username=username)
    else:
        return render_template('index.html')


# Kayıt olma route'u
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Şifreyi hashle (pbkdf2:sha256 kullanıyoruz)
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Kullanıcıyı veritabanına ekle
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Kayıt başarıyla tamamlandı!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')


# Giriş yapma route'u
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Kullanıcıyı veritabanında ara
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):  # Şifreyi doğrula
            session['user_id'] = user.id  # Kullanıcıyı oturumda sakla
            session['username'] = user.username  # Kullanıcı adını sakla
            flash(f'Hoşgeldiniz, {user.username}!', 'success')  # Flash mesajı ile hoşgeldiniz mesajı
            return redirect(url_for('home'))  # Anasayfaya yönlendir
        else:
            flash('Hatalı kullanıcı adı veya şifre.', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')


# Çıkış yapma route'u
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Çıkış yapıldı.', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    # Veritabanı tablolarını oluştur
    create_tables()  # Create the tables if necessary
    app.run(debug=True)
