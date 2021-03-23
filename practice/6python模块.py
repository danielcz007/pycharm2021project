# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 22:11
# @Author  : Daniel
'''
    模块
        - 包含python定义的语句为文件
        - .py文件
        - 作为脚本运行

        模块的导入
            - import 模块名
            - from <模块名> import <方法|变量|类>
            - from <模块名> import*
            - 注意：
                - 同一个模块写多次，但只被导入一次
                - import应该放在代码的顶端
        模块的分类
            - 系统内置模块
            - 第三方的开源模块
            - 自定义模块

'''
import yaml
import requests

import sys

print('命令行参数如下：')
for i in sys.argv:
    print(i)
print('\n\npython 路径为：', sys.path, '\n')