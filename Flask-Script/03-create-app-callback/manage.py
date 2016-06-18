from flask_script import Manager

from app import create_app, db


manager = Manager(create_app)

# 서버 실행
if __name__ == '__main__':
    manager.add_option('-c', '--config', dest='config', required=False, default='config')
    manager.run()
