import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "jhasmin123+-*/abcd")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "parcial.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
