import os

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    # 초기화
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' \
        + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    
    # 외부 확장 초기화
    db.init_app(app)

    # 블루프린트 등록
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')
    
    # 에러 처리    
    @app.errorhandler(404)
    def page_not_found(e):
        return 'Page Not Found'

    return app
