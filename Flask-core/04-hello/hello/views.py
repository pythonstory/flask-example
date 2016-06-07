from . import app

# 뷰 함수와 라우팅
@app.route('/')
def index():    
    return '<h1>Hello World!</h1>'
