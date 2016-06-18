import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config=None):
    # 초기화
    app = Flask(__name__)

    # 앱 설정 로드
    app.config.from_object(config)

    # 외부 확장 초기화
    db.init_app(app)    
    
    # 뷰 함수와 라우팅 (실무에서는 블루프린트 등록 처리)
    @app.route('/')
    def index():    
        return '<h1>Hello World!</h1>'

    return app
