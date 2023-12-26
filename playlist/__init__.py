from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from playlist.config import Config
from flask_cors import CORS

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    CORS(app)
    # Configure your Flask app here (e.g., database URI)
    app.config.from_object(Config)

    db.init_app(app)

    from playlist.main.routes import application
    app.register_blueprint(application)

    return app
