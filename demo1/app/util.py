#!/usr/bin/env python
# coding:utf-8 
# +------------------------------------------
# | author: guijianliang
# | date： 2018/9/26 16:08
# +------------------------------------------
 

from flask import json
from bson import json_util,ObjectId


def bosn_to_json(data):
    return json.dumps(data,default=json_util.default)


def bosn_obj_id(id):
    return ObjectId(id)






































