# -*- coding: utf-8 -*-
import re
import os
source = 'JUx1254dd JUX-123 dddddd--sdsfjlksdjflkadfj打扫房间看圣诞节覅人dsfjlksajdf-( 测试达人,df,电费)~JP.mkv'
patter1=re.compile('[a-zA-Z]{1,9}')
patter2=re.compile('\\d{1,9}')
print(patter1,'-----',patter2)
result1 = re.search(patter1, source)
result2 = re.search(patter2, source)
'''
group() 返回被 RE 匹配的字符串
start() 返回匹配开始的位置
end() 返回匹配结束的位置
span() 返回一个元组包含匹配 (开始,结束) 的位置
group() 返回re整体匹配的字符串，可以一次输入多个组号，对应组号匹配的字符串。
a. group（）返回re整体匹配的字符串，
b. group (n,m) 返回组号为n，m所匹配的字符串，如果组号不存在，则返回indexError异常
c.groups（）groups() 方法返回一个包含正则表达式中所有小组字符串的元组，从 1 到所含的小组号，通常groups()不需要参数，返回一个元组，元组中的元就是正则表达式中定义的组。
'''
print(result1.group())
print(type(result1.group()))
print(result1.group(0))
print(type(result1.group(0)))
print(result2.group(0))
result3=re.findall(patter1, source)
result4=re.findall(patter2, source)
print(result3)
print(result4)

'''
命令：re.sub(pattern, repl, string, count=0, flags=0)
re.sub 用于替换字符串的匹配项。如果没有匹配到规则，则原字符串不变。
第一个参数：规则 
第二个参数：替换后的字符串 
第三个参数：字符串 
第四个参数：替换个数。默认为0，表示每个匹配项都替换
'''
print(re.sub(patter2,'asdflkjasdfkljklasdfjklasdj',source,count=0))
print(patter1.sub('KBKK',source,count=0))