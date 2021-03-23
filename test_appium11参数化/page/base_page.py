#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pycharm2021project 
@File    ：base_page.py
@IDE     ：PyCharm 
@Author  ：Daniel
@Date    ：2021/3/20 14:22 
'''
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 为了应对弹窗问题，导致找不到元素，使用黑名单(黑名单中的元素就是弹窗的元素，如果检测到黑名单中的元素说明出现了弹窗)
    _black_list = []
    _error_cont = 0    # 为了避免黑名单元素查不到进入死循环（元素找不到，并不是因为黑名单中的弹窗问题导致，那么会进入死循环）设置错误次数以及错误最大值
    _error_max = 10
    # 需要传入 dirver ，并声明driver的类型，这样 self.  的时候就可以访问driver的方法了
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # by 为定位方式(by 为tuple 可能为一个也可能为多个，所以需要进行判断)；locator为 元素
    def find(self, by, locator=None):
        # 三目表达式 首先判断 locator 元素 是不是多个（注意用的是elements），如果是的话，传元组tuple；如果不是多个的话（
        # 注意用的是 element 没有 s ），就传 一个 locator
        try:  # 因为有时候定位不到元素，所以需要应对找不到元素的情况; 比如弹窗问题，
            element = self.driver.find_elements(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
            self._error_cont = 0
            return element
        except Exception as e:
            # 如果错误次数大于设置的最大值，为避免进入死循环，直接跳出，抛出异常
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            # 检测黑名单元素 ，并消除
            for black in self._black_list:
                # elements 如果列表长度大于0 说明黑名单中有元素，那么就是查找黑名单中的元素，并对第一个元素进行 点击（消除弹窗）
                # 然后调用方法自身，循环查找，直至黑名单元素消失
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.driver.find(by, locator)
            raise e
    # 读取yaml文件
    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            # steps = yaml.safe_load(f)
            # 声明 steps 的类型为一个列表，且列表里面是 字典 key：value，这样的话 下面使用时 通过“.”就可以访问到对应的方法
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])


