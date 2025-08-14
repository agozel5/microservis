🧩 Microservice: Flask ile Kullanıcı Yönetimi Uygulaması

Bu proje, Flask kullanarak geliştirilen basit bir kullanıcı yönetim mikroservisidir. Kullanıcı kayıt, giriş ve çıkış işlemleri güvenli bir şekilde gerçekleştirilir. Veriler SQLite veritabanında saklanır, şifreler hashlenerek korunur.

🚀 Proje Özeti

Flask ile geliştirilen bu mikroservis:

Yeni kullanıcıların kayıt olmasını,

Kayıtlı kullanıcıların güvenli bir şekilde giriş yapmasını,

Giriş yapan kullanıcıların çıkış yapabilmesini sağlar.

Veritabanı işlemleri SQLAlchemy ile yönetilir ve şifre işlemleri için Werkzeug kütüphanesi kullanılır.

🛠️ Kullanılan Teknolojiler

Flask: Web uygulaması framework'ü

SQLAlchemy: Veritabanı yönetimi için ORM

Werkzeug: Güvenli şifre hashleme

SQLite: Hafif ve gömülü veritabanı çözümü

⚙️ Özellikler

🔐 Kayıt Olma (Signup): Kullanıcılar kayıt olabilir, şifreler hashlenerek saklanır.

✅ Giriş Yapma (Login): Doğrulama sonrası kullanıcı oturumu başlatılır.

🔓 Çıkış Yapma (Logout): Oturum sonlandırılır.

🗃️ Veritabanı Yönetimi: Kullanıcı verileri güvenli bir şekilde SQLite üzerinde saklanır.

📁 Proje Dosya Yapısı
microservis/
│
├── app.py               # Ana uygulama dosyası
├── templates/           # HTML şablonları (signup, login, home, logout)
├── static/              # Statik dosyalar (isteğe bağlı)
└── requirements.txt     # Gerekli paketler

🧪 Uygulama Akışı

Flask uygulaması çalıştırıldığında http://127.0.0.1:5000 adresinden erişilir:

Kayıt Olma: /signup sayfasında kullanıcı adı ve şifre ile kayıt yapılır.

Giriş Yapma: /login sayfasında kullanıcı adı ve şifre ile doğrulama yapılır.

Çıkış Yapma: /logout işlemi ile kullanıcı oturumu sonlandırılır.

🖼️ Ekran Görüntüleri

Kayıt Ekranı: Kullanıcı adı ve şifre alanı

Giriş Ekranı: Giriş için form

Anasayfa: Hoş geldiniz mesajı

Çıkış Ekranı: "Çıkış yapıldı" bildirimi

📸 Not: Ekran görüntülerini screenshots/ klasörüne ekleyip burada gösterebilirsiniz.

✅ Sonuç

Bu proje, mikroservis mimarisiyle kullanıcı yönetimi işlemlerini basit, güvenli ve modüler bir şekilde sunar. Flask ve SQLite gibi hafif teknolojilerle hızlıca geliştirilebilir ve ölçeklenebilir sistemlere temel oluşturabilir.

🔗 Bağlantılar

📂 Kodlara erişmek için GitHub deposunu ziyaret edebilirsiniz:
👉 https://github.com/agozel5/microservis.git
