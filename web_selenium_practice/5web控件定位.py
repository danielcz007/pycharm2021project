#*- coding: utf-8 -*-# @Time    : 2021/2/22 22:44+
# @Author  : Daniel
'''

'''
from selenium import webdriver
from time import sleep

class Test_baidu:
    def __init__(self):
        driver = webdriver.Chrome()
        url = "https://www.baidu.com"
        driver.get(url)

    def test_baidurebang(self):

