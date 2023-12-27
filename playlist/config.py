import os


class Config:
    DB_USERNAME = os.getenv('DB_USERNAME', 'prakhar')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'flask_db')

    # Building the database URI
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    TESTING = True
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USERNAME = os.getenv('DB_USERNAME', 'postgres')
    DB_NAME = os.getenv('DB_NAME', 'test_db')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USERNAME}@{DB_HOST}/{DB_NAME}'
