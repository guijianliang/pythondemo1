#!/usr/bin/env python
# coding:utf-8 
# +------------------------------------------
# | author: guijianliang
# | date： 2018/9/26 17:53
# +------------------------------------------


from flask import Flask
from flask_pymongo import PyMongo
from .config import config
from flask_login import LoginManager,login_user
from .util import bosn_to_json, bosn_obj_id
from app.models.models import User
from flask.logging import create_logger
from flask_uploads import UploadSet, configure_uploads, ALL
import os



mongo = PyMongo()
login_manger = LoginManager()

@login_manger.user_loader
def load_user(user_id):
    user = None
    db_user = mongo.db.users.find_one({"_id":bosn_obj_id(user_id)})
    if db_user is not None:
        user_id = db_user.pop('_id')
        user = User(user_id,extras=db_user)
    return user



def create_app(config_name='dev'):
    app = Flask(__name__)

    # 导入配置
    app.config.from_object(config[config_name])

    # 上传时需要配置的
    # app.config['UPLOADED_PHOTO_DEST'] = os.path.dirname(os.path.abspath(__file__))
    # app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES
    app.config['UPLOAD_FOLDER'] = '../'


    # 初始化mongo
    mongo.init_app(app)
    create_logger(app)



    # 初始化后jinja中许多功能都可以用,这里的login_manger是login_manger = LoginManager()
    login_manger.init_app(app)

    from .main import main as main_blue
    app.register_blueprint(main_blue)

    from .api import api as api_blue
    app.register_blueprint(api_blue)

    return app














































