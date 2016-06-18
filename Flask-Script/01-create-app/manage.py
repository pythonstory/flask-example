from flask_script import Manager

from app import create_app, db


app = create_app()
manager = Manager(app)

# 서버 실행
if __name__ == '__main__':
    manager.run()
