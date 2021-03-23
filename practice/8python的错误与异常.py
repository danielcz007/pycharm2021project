# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 11:21
# @Author  : Daniel
# ================异常==================
'''
    什么是异常？
        错误与异常的区别？
            错误和异常都是程序编译和运行时出现的错误
            而异常可以被开发人员捕捉和处理
            但错误一般是系统错误，一般不需要开发人员处理（也无法处理），比如内存溢出

        那么什么是异常呢？
            异常既是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行
            有些是由于拼写、配置、选项等等各种问题引起的程序错误，有些是由于程序功能处理逻辑不完善引起的漏洞，这些统称为程序中的异常
    异常处理流程：
        检测到错误 --- 引发异常 --- 捕捉异常操作
        异常解决方案：
            拼写错配置等引起的错误，更具出错信息进行排查错误出现的位置进行解决
            程序设计不完善引起的漏洞，根据漏洞的情况进行设计处理漏洞的逻辑
    异常捕捉和异常处理
        try：
            执行代码（被检测）
        except：
            发生异常时执行的代码
        else:
            没有发生异常时执行的代码
        finally:
            不管有没有异常都会执行的代码块
'''

# num1 = int(input("输入一个除数："))
# num2 = int(input("输入一个被除数："))
# print(num1/num2)
# 当被除数为0时，出现异常“ZeroDivisionError: division by zero”
# 当除数或被除数不是数字时，报的异常： ValueError: invalid literal for int() with base 10: 'r'
try:
    num1 = int(input("输入一个除数："))
    num2 = int(input("输入一个被除数："))
    print(num1 / num2)
# except ZeroDivisionError: #把出现的异常放在这里，当出现这个异常时就会被捕捉到
#     print("被除数不能为0")
# except ValueError:
#     print("请输出数字")

# 当我们没有捕捉特定异常时，可以直接不去定义具体的异常
except:
    print("这是一个通用的异常，是由于没有定义具体的异常时，遇到异常就会抛出这个异常")
# 当try中的被检测代码，没有发生异常时，直接走else代码块
else:
    print("程序没有检测到异常")
    #pass
# 无论有没有异常，均会执行的finally中的代码块
finally:
    print("无论发生什么，都会被执行的代码块")
    print("执行结束，请在此输入")

# 自定义异常：我们可以自己定义异常，用于当程序中没有我们需要的异常类型的时候
class MyException(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
# 抛出异常关键字 raise
raise MyException("value3", "value2")