# -*- coding:utf-8 -*-
# @DateTime     : 2019-03-25 13:57 
# @Author       : WangTao master
# @Email        : cs.power.supply@gmail.com
# @FileName     : db_demo01.py
# @Editor       : PyCharm

from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

''' 这是使用flask_sqlalchemy 访问mysql 或者 MariaDB的例子
# DIALECT='mysql'
# DRIVER='pymysql'
# USERNAME='master'
# PASSWORD='djdqltj'
# HOST='192.168.204.128'
# POST='3306'
# DATABASE='master'
# DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,POST,DATABASE)
# SQLALCHEMY_TRACK_MODIFICATIONS=False
'''

app.config.from_object(config)

# app.config['SQLALCHEMY_DATABASE_URI']=DB_URI

db = SQLAlchemy(app)


# 在master数据库中 中创建一张表: 表名为atricle
class Atricle(db.Model):
    __tablename__ = 'atricle'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


db.create_all()


# 将一个列表通过html渲染出来测试
@app.route('/book')
def index():
    books = [{'name': '西游记', 'author': '吴承恩', 'price': 111},
             {'name': '红楼梦', 'author': '曹雪芹', 'price': 121},
             {'name': '水浒传', 'author': '施耐庵', 'price': 131},
             {'name': '三国演义', 'author': '罗贯中', 'price': 141}
             ]
    return (render_template('index.html', book=books))


# 以下是将查出的数据在Html中渲染出
@app.route('/rs')
def rs():

    # 查询后通过HTML渲染
    result = Atricle.query.filter(Atricle.title == 'aaaaaaaa').all()
    if (len(result) == 0):
        return ('查询为空')
    else:
        return (render_template('index01.html', book=result))

if __name__ == '__main__':
    app.run(debug=True)
