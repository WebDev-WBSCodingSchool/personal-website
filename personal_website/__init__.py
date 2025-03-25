from flask import Flask
from .routes import admin_bp, home_bp

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(admin_bp)
    app.register_blueprint(home_bp)

    return app