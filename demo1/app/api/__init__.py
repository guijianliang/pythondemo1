#!/usr/bin/env python
# coding:utf-8 
# +------------------------------------------
# | author: guijianliang
# | date： 2018/9/26 14:18
# +------------------------------------------
 
from flask import Blueprint
api = Blueprint('api',__name__,url_prefix='/api')

# 必须先加载这俩,否则的话,其他地方的路由弄不过来
from . import items
from . import test_url
from . import users


# @api_blue.route('/test1')
# def test1():
#     return 'hehhe'




































