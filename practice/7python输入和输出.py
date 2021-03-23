# -*- coding: utf-8 -*-
# @Time    : 2021/1/30 16:30
# @Author  : Daniel
import io
'''
    字面量插值：
        格式化输出 %s,%d,%f
        format()方法
        f''
'''
#格式化输出
name = "zhangsan"
age = 18

print("我的名字叫%s,年龄是%d" % (name, age))

#通过format()输出
name = "zhangsan"
age = 18

print("my name is {0},age is {1},{0}今年{1}岁啦".format(name, age))

# 列表的解包
lista = ["lisi", 19]
print("my name is {0},age is {1},{0}今年{1}岁啦".format(*lista))
# 元组的解包
tuple_a = ("wangwu",17)
print("my name is {0},age is {1},{0}今年{1}岁啦".format(*tuple_a))
# 字典的解包，注意要在{}中写key的值
dict_a = {"name":"zhaoliu", "age":15}
print("my name is {name},age is {age},{name}今年{age}岁啦".format(**dict_a))

'''
字符串格式化机制(python3.6及以上) Formatted string literals
用法：f'{表达式或者函数}'
注意：{}内不能转义，不能写\
'''
name = "zhangsan"
age = 18
# 变量
print(f"my name is {name},age is {age}")
# 函数
print(f"my name is {name.upper()}")
# 匿名函数，注意函数要加括号
print(f"result is {(lambda x,y:x*y)(2,3)}")
'''
#打开一个文件
f = open("./tempfile/foo.txt", "w")

f.write("python 是世界上最好的语言。\n是的，确实非常好！！\n")

#关闭打开的文件
f.close()
'''
f = open("./tempfile/foo.txt", "r")
str = f.read()
print(str)
f.close()