#!/usr/bin/env python
# coding:utf-8 
# +------------------------------------------
# | author: guijianliang
# | date： 2018/9/21 12:22
# +------------------------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired
# from flask_wtf.html5 import EmailField
from wtforms.fields.html5 import EmailField


class PKForm(FlaskForm):
    pk1 = StringField(validators=[DataRequired()])
    pk2 = StringField(validators=[DataRequired()])
    submit = SubmitField(label='pk一下')


class LoginForm(FlaskForm):
    email =EmailField('邮箱',validators=[DataRequired()])
    password =PasswordField('密码',validators=[DataRequired()])
    submit = SubmitField('登录')


class RegisterForm(FlaskForm):
    email = EmailField('邮箱',validators=[DataRequired()])
    username = StringField('用户名',validators=[DataRequired()])
    password = PasswordField('密码',validators=[DataRequired()])
    repeat = PasswordField('重复密码',validators=[DataRequired()])
    submit = SubmitField('注册')








