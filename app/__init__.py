# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from .filters import formatDate

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    current_config = config[config_name]
    app.config.from_object(current_config)
    current_config.init_app(app)

    db.init_app(app)

    from .snippet import snippet as snippet_blueprint
    app.register_blueprint(snippet_blueprint, url_prefix="/snippet")
    from .downloader import downloader as downloader_blueprint
    app.register_blueprint(downloader_blueprint, url_prefix="/downloader")

    _filters = {'name': 'formatDate'}
    app.jinja_env.filters.update(_filters)

    return app
