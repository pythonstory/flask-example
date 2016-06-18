from flask import Blueprint


main = Blueprint('main', __name__)

# 뷰 함수와 라우팅
@main.route('/')
def index():    
    return '<h1>Hello World!</h1>'
