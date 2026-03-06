from flask import Flask

from .extensions import db


def create_app(config_object: str = "config.Config") -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    db.init_app(app)

    from . import routes

    app.register_blueprint(routes.bp)

    with app.app_context():
        db.create_all()

    return app
