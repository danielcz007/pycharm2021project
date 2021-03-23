# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 11:22
# @Author  : Daniel
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

# 登陆页面PO
#from web_selenium_practice.yanlian_webauto.index_page import RegisterPage
from webUI.webUIdemo1.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    def scan(self):
        '''
        扫码
        :return:
        '''
        pass

    def goto_register(self):
        '''
        跳转至注册页
        :return:
        '''
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return RegisterPage(self.driver)