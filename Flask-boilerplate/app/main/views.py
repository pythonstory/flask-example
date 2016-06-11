# -*- coding: utf-8 -*-
from flask import render_template
from flask_babel import format_datetime
from datetime import datetime

from . import main


@main.route('/')
def index():

    print(format_datetime(datetime(1987, 3, 5, 17, 12)))

    return render_template('default/main/index.html')
