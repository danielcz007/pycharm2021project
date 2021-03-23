# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 18:09
# @Author  : Daniel
'''
    selenium 的安装：
        官方：https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
            eg chrome浏览器88版本:https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/
        下载好之后：位置在 D:\drivers\chromedriver20210220_88\chromedriver_win32
        然后配置环境变量：path中添加 上述位置
        在cmd模式下 查看安装  chromedriver
        重启命令行以及pycharm：https://ceshiren.com/t/topic/58/2
'''
import selenium
from time import sleep
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    sleep(5)
test_selenium()