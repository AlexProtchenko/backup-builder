from flask import Flask

from src.builder.controller import builder_service


def create_app():
    app = Flask("builder-service")

    app.register_blueprint(builder_service)

    return app
