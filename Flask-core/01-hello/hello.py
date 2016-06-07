from flask import Flask


# 초기화
app = Flask(__name__)

# 뷰 함수와 라우팅
@app.route('/')
def index():    
    return '<h1>Hello World!</h1>'

# 서버 실행
if __name__ == '__main__':
    app.host = '127.0.0.1'
    app.port = 5000
    app.debug = True
    
    app.run()
    