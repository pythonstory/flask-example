# -*- coding: utf-8 -*-
from flask import Blueprint

main = Blueprint('main', __name__, url_prefix='/')
#main = Blueprint('main', __name__, url_prefix='/<lang_code>/main')

from . import views, errors
