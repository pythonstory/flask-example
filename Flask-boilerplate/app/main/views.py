# -*- coding: utf-8 -*-
from . import main


@main.route('/')
def index():
    return 'main blueprint home'
