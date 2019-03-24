# -*- coding: utf-8 -*-
from tkinter import scrolledtext
import re
import os
import pathlib
from tkinter import *
from tkinter.filedialog import askdirectory


def fh(source):
    patter1 = r'^[a-zA-Z]{1,9}'
    patter2 = r'\d{1,9}'
    patter3 = r'(?<=\().*(?=\))'

    """ 
    (?<=exp)是以exp开头的字符串, 但不包含本身.
    (?=exp)就匹配惟exp结尾的字符串, 但不包含本身.
    (?<=\()    也就是以括号开头, 但不包含括号.
    (?=\)) 就是以括号结尾
     """

    result1 = re.search(patter1, source)
    result2 = re.search(patter2, source)
    result3 = re.search(patter3, source)

    if (result1 and result2 and result3):
        ree = '番号：' + result1.group(0) + '  编号：' + \
            result2.group(0) + '  主演：' + result3.group(0)
        return (ree)
    else:
        return ("not re")


"""
ssssss=os.getcwd() #当前所在目录
s1=os.path.dirname(os.getcwd())
s2=os.path.dirname(s1)
s3=os.path.dirname(__file__)
print(ssssss) 
print('------------------')
path_str='c:\\Python37'
sss=os.path.abspath('test02.py')
print(os.path.dirname(sss)) #返回目录名
print(os.path.basename(sss)) #返回文件名
print(os.path.split(sss)) #返回 目录+文件的 元组对象
m=os.path.exists(path_str)
if m:
    print('目录存在')
else:
    print('目录不存在')
"""
file_count = 0


def print_dir_conns(sPath, i):
    global file_count
    hzm_name = ['mkv', 'mp4']
    for schild in os.listdir(sPath):
        schildPath = os.path.join(sPath, schild)

        if os.path.isdir((schildPath)):
            print_dir_conns(schildPath, i)
        else:

            hzm = os.path.basename(schildPath).split('.')
            if hzm[-1] in hzm_name:
                print(str(i) + '-----' +
                      os.path.basename(schildPath) + '后缀名=======>' + hzm[-1] + '格式化番号为：' + fh(
                    os.path.basename(schildPath)))
                i = i + 1
                file_count = file_count + 1
    print('一共找到：%d,i=%d' % (file_count, i))


# print_dir_conns('o:\\外挂中字',0)

iii = 0
ddd = 0


def pd_dir(dir_name):
    entries = pathlib.Path(dir_name)
    # print(entries.parents)
    for entry in entries.iterdir():
        if entry.is_dir():
            # print(entry.name,'--目录')
            # print(d)
            pd_dir(entry)
        elif entry.is_file():
            if str.strip(str.lower(entry.suffix)) in ['.mkv', '.avi', '.wmv', '.mp4']:
                print(entry.name, '--文件')

                global iii
                iii = iii + 1
                print('文件数=%d' % iii)
                # print(entry.suffix)
        else:
            print('无效文件')


print(str(iii) + '--------------' + str(ddd))

# 使用path.rglob 递归所有文件，不含目录


def pd_dir2(dir_name):
    count = 0
    for ss in pathlib.Path(dir_name).rglob('*'):
        if str.strip(str.lower(ss.suffix)) in ['.mkv', '.avi', '.wmv', '.mp4']:
            count += 1
            # print(ss)
            print(str(count), '--', ss.resolve())  # 绝对路径和文件名
            # print(pathlib.PureWindowsPath(ss.resolve()).parent)  # 返回所有上级（祖先）目录列表，[上级目录, 上上级目录, …, 根目录]

# pd_dir2('o:/外挂中字/')


def selectPath():
    path_ = askdirectory()
    path.set(path_)
    # global  file_path_s # 尼玛这么写会被开除的
    # file_path_s=path_


def print_path():
    pd_dir2(en.get())
    # pass


root = Tk()
root.title = ('TK 正在测试。。。。')
path = StringVar()

Label(root, text="目标路径:").grid(row=0, column=0)
en = Entry(root, textvariable=path)
en.grid(row=0, column=1)
Button(root, text="路径选择", command=selectPath).grid(row=0, column=2)
Button(root, text="确认", command=print_path).grid(row=0, column=3)
root = Tk()

# 滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）
scr = scrolledtext.ScrolledText(root, width=70, height=13)
scr.place(x=50, y=50)

root.mainloop()
