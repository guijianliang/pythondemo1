#!/usr/bin/env python
# coding:utf-8 
# +------------------------------------------
# | author: guijianliang
# | date： 2018/9/21 10:19
# +------------------------------------------

'''
将所有的路由都先写到这里
'''



# 编写蓝本
from flask import Blueprint,render_template,request
from app.forms import PKForm,LoginForm


# url_prefix='/api' 目的是在前面加上/api,如果不需要刻意取消
# main = Blueprint('main',__name__,url_prefix='/api')
main = Blueprint('main',__name__)

@main.route('/test')
def test():
    return 'test.'

@main.route('/')
def index():
    pk_form = PKForm()
    return render_template('index.html', form=pk_form)

# @main.route('/login')
# def login():
#     render_template('login.html')


@main.route('/pk',methods=['GET','POST'])
def pk():
    # pk_form = PKForm(request.form)
    pk_form = PKForm()
    if pk_form.validate_on_submit():
        pk1_name = request.form.get('pk1')
        pk2_name = request.form.get('pk2')
        return render_template('pk.html', pk1=pk1_name, pk2=pk2_name)
    return 'invalid input'


# 这个需要写在最后面,否则会报错
from . import errors,views




























