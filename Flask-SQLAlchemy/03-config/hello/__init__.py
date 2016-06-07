from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 초기화
app = Flask(__name__)

# 설정 파일 로드
app.config.from_object('config.Configuration')

db = SQLAlchemy(app)