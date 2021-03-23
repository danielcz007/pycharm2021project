# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 15:37
# @Author  : Daniel
'''
    os      操作系统相关
    time    时间与日期
    urllib  网络请求
    math    科学计算
'''


'''
    os模块
        os模块主要是对文件，目录的操作
        常用方法：
            os.makdir() 创建目录
            os.removedirs()     删除文件
            os.getcwd()    获取当前目录
            os.path.exists(dir or file)     判断文件或者目录是否存在
'''
'''
import os
import random

nums = random.randint(0, 100)
name = "testdir" + str(nums)

print(name)
print(os.getcwd())  #返回当前的工作目录 有点类似linux的pwd
os.mkdir("./tempfile/"+name)    #以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
print(os.listdir("./tempfile"))     #返回path指定的文件夹包含的文件或文件夹的名字的列表，类似linux中的 ls
os.removedirs("./tempfile/"+ name)  #递归删除目录。
print(os.listdir("./tempfile"))
'''
'''
    time模块
        获取当前时间以及时间格式的模块
        导入方式：import time
        time模块常用方法：
            time.asctime()   国外的时间格式
            time.time()      时间戳
            time.sleep()     等待
            time.localtime() 时间戳转成时间元组
            time.strftime()  将当前的时间戳转成带格式的时间 strftime(format, p_tuple=None)
                格式：time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())
'''
'''
import time

now = time.time()
west_time = time.asctime()
now_tup = time.localtime()
format_time = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())

print(now)
print(west_time)
print(now_tup)
print(format_time)

#获取两天前的时间
two_day_befortime = now - 2*24*60*60
two_day_tup = time.localtime(two_day_befortime)
two_day_formattime = time.strftime("%Y-%m-%d  %H:%M:%S", two_day_tup)

print(two_day_formattime)
'''
'''
    urllib库：有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:
    
'''
'''
import urllib.request

# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.status)

response: object = urllib.request.urlopen('http://www.baidu.com')
print(response.status)
print(response.read())
print(response.headers)
'''

import math

print(math.ceil(5.6))