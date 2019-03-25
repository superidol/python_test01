# -*- coding:utf-8 -*-
# @DateTime     : 2019-03-18 10:31 
# @Author       : WangTao master
# @Email        : cs.power.supply@gmail.com
# @FileName     : app.py
# @Editor       : PyCharm
from flask import Flask,url_for,redirect,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
db=SQLAlchemy(app)


# 使用渲染模板(对HTML文件进行变量传递)
# HTML文件放在templates目录下
# 从Flask中import reader_templateh函数
# 传递的变量可以直接使用字典方式 接受HTML中 用 {{变量名}} 双花括号
# 也可以传递字典或者对象,接受HTML 用{{变量.参数}}处理



@app.route('/<ppp>')
def hello_world(ppp):
    # 定义一个类
    class mov(object):
        name="WangTao"
        age=60
        sex="MR"
    p=mov()
    # 从浏览器URL接受参数,再传递到HTML ,注意这里的接收的参数为字符.
    user_list = {'name': 'superidol', 'age': '18', 'gender': '男','p':p,'ppps':ppp}
    return(render_template('index01.html',**user_list))



# 从浏览器传递参数    transmit【英文为传递的意思】
# 1、参数需要放在‘<>’中间，
# 2、视图函数中需要放和URL中同名的参数

@app.route('/help/<id>')
def transmit_id(id):
    return ('你传递的参数是：%s' % id)


# 反转URL
# 从视图函数到URL的转换叫反转URL
#     用于：页面重定向，如指向登录界面等，页面结束，跳转到首页等，可以直接指向视图函数名称。


@app.route('/my_list')
def my_list_0000():
    print('你的视图函数名称是：%s' % url_for('my_list_0000'))
    print ('你的视图函数名称是：%s' % url_for('transmit_id',id='123'))
    return (url_for('my_list_0000'))

if __name__=='__main__':
    app.run(debug=True)
