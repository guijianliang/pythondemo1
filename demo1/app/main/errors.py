#!/usr/bin/env python
# coding:utf-8 
# +------------------------------------------
# | author: guijianliang
# | date： 2018/9/21 12:27
# +------------------------------------------

from flask import render_template
from . import main

'''
# 这个需要写在最后面,否则会报错,需要在init中导入errors,否则会报错
from . import errors,views
'''
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
