#!/usr/bin/env python
# coding:utf-8 
# +------------------------------------------
# | author: guijianliang
# | date： 2018/10/10 18:35
# +------------------------------------------

from app.api import api
from ..forms import RegisterForm, LoginForm
from flask import flash, redirect, url_for, render_template, request, current_app, g, jsonify
from flask import json, abort,send_from_directory,make_response,send_file
from .. import mongo
from ..models.models import User
from flask_login import login_user
from flask_httpauth import HTTPBasicAuth
from app.util import bosn_to_json, bosn_obj_id
from werkzeug.utils import secure_filename
import os
from collections import OrderedDict
import math

'''
这里面的api需要先登录,获取到一个token后才能继续访问resource等api
'''

auth = HTTPBasicAuth()


# 配置上传,flask_uploads
# photos = UploadSet('PHOTO')
# configure_uploads(app, photos)


@auth.verify_password
def verify_password(email_or_token, password):
    user = User.verify_auth_token(email_or_token)
    if user is None:
        user = mongo.db.users.find_one({'email': email_or_token})
        if not user:
            return False
        else:
            if not User.verify_passwd(user['password'], password):
                return False
    g.current_user = User(user.pop('_id'), extras=user)
    return True


@api.route('/token')
@auth.login_required
def get_auth_token():
    token = g.current_user.gen_auth_token(3600)
    return jsonify({'token': token.decode('ascii'), 'duration': 3600})


@api.route('/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'hello,%s!' % g.current_user.username})


# 个人主页
@api.route('/user/<username>')
@auth.login_required
def user(username):
    # user = {'username':'guijianliang','avatar':'https://www.gravatar.com/avatar/729e26a2a2c7ff24a71958d4aa4e5f35'}
    # posts = [
    #     {'author': user, 'body': 'Test post #1kdkjdkjkdsjfksdjfksdjfksjdfksjdkfjsdkfjskdjfksdjfkdsjfkdjfkdjfkdjfkdjfkdjfkdjkfdkdk'},
    #     {'author': user, 'body': 'Test post #2'}
    # ]

    _posts = mongo.db.posts.find({'username': username})
    _list = []
    for i in _posts:
        _i = json.loads(bosn_to_json(i))

        # 删除id数据,也可以不删除;
        del (_i['_id'])
        # print(_i)
        _list.append(_i)

    print(_list)
    # user = {'username':_posts['username'],'avatar':_posts['avatar']}
    posts = _list

    return render_template('users.html', user=user, posts=posts)


# publish_article,用于发表文章的接口
@api.route('/publish_article/<username>')
@auth.login_required
def publish_article(username):
    pass
    # return render_template('publish_article.html', user=user, posts=posts)


# 上传文件的接口
# 允许上传的文档的类型
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'gif', 'pdf', 'doc'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.route('/upload', methods=['POST', 'GET'])
@auth.login_required
def upload():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            flash('没有上传file', 'WARNING')
            return redirect(request.url)

        file = request.files['file']
        print(file.filename)
        if file == '':
            flash('上传文件为空', 'WARNING')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('app/uploads', file.filename))
            # flash('保存成功','SUCCESS')
            return redirect(url_for('api.upload', filename=filename))

    return render_template('upload.html')


@api.route('/test_books', methods=['POST', 'GET'])
@auth.login_required
def test_books():
    page = 1
    pathDir = os.listdir('app/uploads')
    print(pathDir)
    # d = ['1', '2', '3']
    # test_dict = {'1':'hhe','2':"hahahahah"}
    _dict = OrderedDict()
    page_dict = OrderedDict()
    for index,item in enumerate(pathDir,start=1):
        _dict[str(index)] = item
    # _dict['book_len'] = len(pathDir)
    print(_dict)
    try:
        page = int(request.args['page'])
        if request.args['page'] != '':
            if page*2 <= len(pathDir):
                start = 2 * page - 1
                end = 2 * page + 1
            else:
                start = 2 * page - 1
                end = len(pathDir)+1
            for _i in range(start,end):
                page_dict[_i] = _dict[str(_i)]
                print('-----')
                print(page_dict[_i])

    except Exception as e:
        print(e)
        for _i in range(1,3):
            print('+++++')
            page_dict[_i] = _dict[str(_i)]



    # return render_template('test_books.html', dicts=(_dict.items()))
    return render_template('test_books.html', book_list=page_dict,booklength=math.ceil(len(pathDir)/2),p=page,hh=len(pathDir))


# 点击链接的时候会显示预览,或者下载
@api.route('/preview/<item>')
@auth.login_required
def preview_file(item):
    response = make_response(send_file("uploads/"+item))
    return response
























































