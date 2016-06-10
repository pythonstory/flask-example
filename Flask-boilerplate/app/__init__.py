# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config=None, app_name=None):
    app_name = app_name or __name__
    app = Flask(app_name)

    app.config.from_object(config)

    # Flask 확장 초기화
    db.init_app(app)

    # 블루프린트 모듈 등록
    from app.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
