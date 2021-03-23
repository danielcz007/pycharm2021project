# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 18:33
# @Author  : Daniel
'''
    python第三方库： pytest----requests
        安装： pip install pytest/requests
        requests库：官方文档中文：https://requests.readthedocs.io/zh_CN/latest/
'''
import requests
#get请求
r = requests.get('http://www.baidu.com')
print(r.status_code)
#参数化
payload = {'key1': 'value1', 'key2': 'value2'}
r2 = requests.get("http://httpbin.org/get", params=payload)
print(r2.url)
#post请求
r_post = requests.post('http://httpbin.org/post', data={'key':'value'})
print(r_post.text)
print(r_post.encoding)
print(r_post.headers)
print(r_post.status_code)
print(r_post.url)
#参数化
r_post2 = requests.post('http://httpbin.org/post', data=payload)
print(r_post2.text)
print(r_post2.encoding)
print(r_post2.headers)
print(r_post2.status_code)
print(r_post2.url)