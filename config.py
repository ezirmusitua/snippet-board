#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'db/snippet_board.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
