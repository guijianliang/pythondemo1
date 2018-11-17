#!/usr/bin/env python
# coding:utf-8
# +------------------------------------------
# | author: guijianliang
# | date： 2018/9/26 15:32
# +------------------------------------------

# from app import mongo
from flask import request
from flask.views import MethodView
from app.util import bosn_to_json, bosn_obj_id
import json
from .. import mongo
from . import api

class ItemAPI(MethodView):
    def get(self, item_id):
        if item_id is not None:
            item = mongo.db['test'].find_one({'_id': bosn_obj_id(item_id)})
            return bosn_to_json(item)
        params = {}
        for k, v in request.args.items():
            if v:
                params['attributes.' + k] = v.strip()
            cursor = mongo.db['test'].find(params)
            items = [bosn_to_json(item) for item in cursor]
            return json.dumps(items)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


# 类似于路由
item_view = ItemAPI.as_view('item_api')
api.add_url_rule('/items/', defaults={'item_id': None}, view_func=item_view, methods=['GET',])
# api.add_url_rule('/items/', view_func=item_view, methods=['GET',])
api.add_url_rule('/items/', view_func=item_view, methods=['POST',])
api.add_url_rule('/items/<item_id>', view_func=item_view, methods=['GET', 'DELECT', 'PUT'])
