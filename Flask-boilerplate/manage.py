# -*- coding: utf-8 -*-
from flask_script import Manager

from app import create_app

# create_app function is passed  as a callback.
manager = Manager(create_app)

if __name__ == '__main__':
    manager.add_option('-c', '--config', dest='config', required=False, default='config')
    manager.run()
