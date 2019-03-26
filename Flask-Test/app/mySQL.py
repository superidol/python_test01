# -*- coding:utf-8 -*-
# @DateTime     : 2019-03-26 15:41 
# @Author       : WangTao master
# @Email        : cs.power.supply@gmail.com
# @FileName     : mySQL.py
# @Editor       : PyCharm

import pymysql
from flask import Flask, redirect, render_template



app = Flask(__name__)


# def db_connect(sql):
#     db = pymysql.connect("192.168.204.128", "master", "djdqltj", "master")
#     cursor = db.cursor()
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     return results
#     # for row in results:
#     #     print(row)


@app.route('/mysql-demo')
def index():
    sql = 'select * from atricle'
    # db_connect(sql)
    db = pymysql.connect("192.168.204.128", "master", "djdqltj", "master")
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    rs = results
    db.close()
    # for row in results:
    #     print(row[0])
    return (render_template('index02.html',book=rs))


if __name__ == '__main__':
    app.run(debug=True)
