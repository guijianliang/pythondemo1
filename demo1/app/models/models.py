#!/usr/bin/env python
# coding:utf-8 
# +------------------------------------------
# | author: guijianliang
# | date： 2018/9/26 19:26
# +------------------------------------------


from flask import current_app
from flask_login import UserMixin
# 导入TimedJSONWebSignatureSerializer，用于生成具有过期时间的JSON Web签名。
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash
from ..util import bosn_to_json, bosn_obj_id

import json


class User(UserMixin):
    def __init__(self, user_id, extras=None):
        self.id = user_id
        if (extras is not None) and isinstance(extras, dict):
            for name, attr in extras.items():
                setattr(self, name, attr)
                #setattr() 函数对应函数 getattr()，用于设置属性值，该属性必须存在


    @staticmethod
    def gen_passwd_hash(password):
        return generate_password_hash(password)

    @staticmethod
    def verify_passwd(passwd_hash,password):
        return check_password_hash(passwd_hash,password)

    def gen_auth_token(self,expiration):
        s = Serializer(current_app.config['SECRET_KEY'],expires_in=expiration)
        return s.dumps(bosn_to_json({'id':self.id}))

    @staticmethod
    def verify_auth_token(token):
        from app import mongo
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        _dict = json.loads(data)
        return mongo.db.users.find_one({'_id':bosn_obj_id(_dict['id']['$oid'])})



