# -*- coding: utf-8 -*-
from flask import url_for, render_template

from . import main


@main.route('/')
def index():
    return render_template('default/main/index.html')
