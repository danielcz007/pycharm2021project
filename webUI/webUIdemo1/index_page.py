# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 11:18
# @Author  : Daniel

from selenium import webdriver
from selenium.webdriver.common.by import By
from webUI.webUIdemo1.login_page import LoginPage
from webUI.webUIdemo1.register_page import RegisterPage

# 首页PO
# 元素定位 优先级  优先使用ID  ，如果没有就是用CSS_SELECTOR
class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        '''
        进入登陆页面
        ：return：
        '''
        # click login button
        # return LoginPage
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # 把driver 传给loginpage  这样就不用再loginpage中再次声明 driver乐
        return LoginPage(self.driver)

    def goto_register(self):
        '''
                进入注册页面
                ：return：
        '''
        # click register button
        # return RegisterPage
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return RegisterPage(self.driver)

