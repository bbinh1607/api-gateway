from flask import Flask
from backend.config import Config
from backend.api.api_gateway import getway_bp


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config.from_object(Config)
    app.register_blueprint(getway_bp)
    return app
