# -*- coding: utf-8 -*-
from flask import render_template
from flask_babel import gettext

from . import main


@main.route('/')
def index():
    print(gettext('Home'))
    return render_template('default/main/index.html')
