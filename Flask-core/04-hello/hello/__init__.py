from flask import Flask


# 초기화
app = Flask(__name__)

# 설정 파일 로드
app.config.from_object('config.Configuration')
