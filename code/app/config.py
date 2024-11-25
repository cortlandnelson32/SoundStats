import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://persoprojects_user:ZfyW2mm6mH0DsGms8w31cPFUOuJplBxw@dpg-ct0csu56l47c73894jfg-a/persoprojects')
    SQLALCHEMY_ECHO = True
