import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hello-world12345.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'hello-world-ny'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacity_ninna'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'password1!'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'helloworld12345'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'v/dl5d9WzdRq0IoRQXhTAR7aX7IKRXiN1p7Ku8NHQ+WxwcA0HGFma+Cn6FeatmXaLOmXBf6tH1yd+AStob8hkw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'