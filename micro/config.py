import os

class Config:
    SECRET_KEY = 'gizli-anahtar'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'jwt-gizli-anahtar'
