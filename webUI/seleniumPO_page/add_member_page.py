# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 14:52
# @Author  : Daniel
# 企业微信首页
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMemberPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self):
        '''
        添加联系人，详细信息
        :return:
        '''
        # 输入用户名
        self.driver.find_element(By.ID, "username").send_keys("cz003")
        sleep(2)
        # 输入账号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("1001001003")
        sleep(2)
        # 输入手机号
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("12345671003")
        sleep(2)
        # 点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        sleep(2)

        return  True