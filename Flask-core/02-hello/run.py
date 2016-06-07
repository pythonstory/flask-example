from hello import app


# 서버 실행
if __name__ == '__main__':
    app.host = '127.0.0.1'
    app.port = 5000
    app.debug = True
    
    app.run()
    