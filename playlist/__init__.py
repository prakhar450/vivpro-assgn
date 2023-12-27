from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from playlist.config import Config, TestConfig

db = SQLAlchemy()


def create_app(config_object=None):
    app = Flask(__name__)

    if config_object is None:
        app.config.from_object(Config)
    else:
        app.config.from_object(TestConfig)

    db.init_app(app)

    from playlist.main.routes import application
    app.register_blueprint(application)

    return app
