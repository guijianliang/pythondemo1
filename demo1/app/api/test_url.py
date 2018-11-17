#!/usr/bin/env python
# coding:utf-8 
# +------------------------------------------
# | author: guijianliang
# | date： 2018/9/26 16:47
# +------------------------------------------

from app.api import api
from ..forms import RegisterForm, LoginForm
from flask import flash, redirect, url_for, render_template, request,current_app,g
from flask import jsonify
from .. import mongo
from ..models.models import User
from flask_login import  login_user
from .users import verify_password

# index
@api.route('/')
def index():
    return render_template('test_bases.html')


# 测试vue
@api.route('/bases')
def test1():
    # flash('<h1>hehhe</h1>','SUCCESS')
    return render_template('test_vue.html')

# 测试继承base的一个页面
@api.route('/test_bases')
def test2():
    return render_template('test_bases.html')

# 测试返回一个json字符串
@api.route('/test3',methods = ['GET','POST'])
def test3():
    return jsonify({'gui':'18'})


# 注册接口
@api.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        uname = form.username.data
        passwd = form.password.data
        re_passwd = form.repeat.data
        if passwd != re_passwd:
            flash('两次密码不一致', 'WARNING')
        elif mongo.db.users.find_one({'email': email}) != None:
            flash('该邮箱已经被注册', 'WARNING')
        else:
            mongo.db.users.insert({'username': uname, 'email': email, 'password': User.gen_passwd_hash(passwd)})
            flash('success')
            return redirect(url_for('.login'))
    return render_template('register.html', form=form)


# 登录接口
@api.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_user = mongo.db.users.find_one({'email': form.email.data})
        # print(db_user)
        current_app.logger.info(db_user)
        if db_user is not None:
            db_passwd = db_user.get('password', None)
            if User.verify_passwd(db_passwd, form.password.data):
                user = User(db_user['_id'])
                login_user(user)  # 塞进login_user
                flash('登录成功', 'SUCCESS')
                verify_password(form.email.data,form.password.data)
                return redirect(request.args.get('next') or url_for('main.index'))
            else:
                flash('邮箱或者密码错误', 'WARNING')
        else:
            flash('不存在用户', 'WARNING')
    return render_template('login.html', form=form)
