# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 14:59
# @Author  : Daniel
# 企业微信首页


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from webUI.seleniumPO_page.add_member_page import AddMemberPage


class MainPage:

    def __init__(self):
        # 复用浏览器，需要设置 option.debugger_address
        '''
        一、前提条件

1、首先需要把Chrome配置到环境变量里

2、把浏览器关闭包括进程等都杀掉

3、在命令行输入以下命令

Windows/Linux命令为：chrome --remote-debugging-port=9222 (9222为端口号，可以换成任意一个没有被占用的端口)
Mac命令为：Google\ Chrome --remote-debugging-port=9222 (9222为端口号，可以换成任意一个没有被占用的端口) (注意命令中间的反斜线)
        '''
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(10)
    def goto_add_member(self):
        '''
        添加成员
        :return:
        '''
        # 定位添加按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)