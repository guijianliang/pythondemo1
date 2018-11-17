#!/usr/bin/env python
# coding:utf-8 
# +------------------------------------------
# | author: guijianliang
# | date： 2018/9/21 16:21
# +------------------------------------------
 
# CSRF_ENABLED = True
# SECRET_KEY = 'you-will-never-guess'
#

import os

# 不知道啥意思
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseConfig:
    SECRET_KEY = 'b0c60788fb46b6c9c9184a51ae46a98c'  #guijianliang进行了MD5
    PKYX_MAIL_SENDER = 'pk一下 <jianliang.gui@nio.com>'
    PKYX_MAIL_SUBJECT_PRE = '[test]'

    @staticmethod
    def init_app(app):
        pass

class DevConfig(BaseConfig):
    # MONGO_HOST = '127.0.0.1'
    # MONGO_PORT = 27017
    # MONGO_DBNAME = 'test'
    MONGO_URI = 'mongodb://localhost:27017/test'

    @staticmethod
    def init_app(app):
        from flask_pymongo import PyMongo
        mongo = PyMongo(app)
        return mongo

config = {'dev': DevConfig}






























