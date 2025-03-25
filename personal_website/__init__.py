from flask import Flask
from .routes import home_bp

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(home_bp)

    return app