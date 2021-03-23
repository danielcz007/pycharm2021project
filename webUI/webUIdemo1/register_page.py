# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 11:23
# @Author  : Daniel

# register注册页面PO
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    # driver: WebDriver  类型提示，执行参数类型，这样的话 使用driver “.” 时 就可以联想出对应的方法
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.ID, "corp_name").send_keys('大地')
        self.driver.find_element(By.ID, "manager_name").send_keys("daniel")
        self.driver.find_element(By.ID, "register_tel").send_keys("12345678901")
        self.driver.find_element(By.ID, "submit_btn").click()

        return True


