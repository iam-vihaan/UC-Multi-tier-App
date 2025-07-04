from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
