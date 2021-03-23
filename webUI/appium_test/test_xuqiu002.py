#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    @Project ：pycharm2021project
    @File    ：test_xuqiu002.py
    @IDE     ：PyCharm
    @Author  ：daniel
    @Date    ：2021/3/13 15:32
'''
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW:
    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "noReset": True,  # 不重置
            #"dontStopAppOnReset": True,  # 执行结束后不停止app，可继续使用
            "skipDeviceInitialization": True  # 跳过安装和权限设置
            #"unicodeKeyBoard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_serch(self):
        print("搜索测试用例")
        '''
        1. 打开雪球 app
        2.点击搜索框
        3.输入“阿里巴巴”
        4.在搜索结果里，点击“阿里巴巴”
        5.获取这只上 香港的埃里巴巴的股价，并判断  ，这支股票的价格大于200
        '''
        els_search = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        els_search.click()
        els_search_input = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # 选择"阿里巴巴-SW"
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
        # 获取股价 因为根据价格id查找元素时，有重复的id，所以获取全部id 放入list，然后根据下标查找，但是不够灵活，可能有更多个股票价格，而顺序可能会变动
        # current_price = float(self.driver.find_elements_by_id("com.xueqiu.android:id/current_price")[1].text)
        # Xpath高级用法  已知 需要获取股票“阿里巴巴-SW”的股票价格，所以获取路径，然后去找 父节点的父节点 ，然后再找 去相对路径查找 价格的id（因为价格有重复，所以不能单一使用id定位）
        current_price = float(self.driver.find_element_by_xpath("//*[@text='阿里巴巴-SW']/../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        print(current_price)
        assert current_price > 200

    def test_attr(self):
        '''
        ◆打开【雪球】应用首页今定位首页的搜索框
        ◆判断搜索框的是否可用并查看搜索框name属性值
        ◆打印搜索框这个元素的左上角坐标和它的宽高
        ◆向搜索框输入: alibaba
        ◆判断【阿里巴巴】是否可见
        ◆如果可见,打印“搜索成功”点击,如果不可见,打印“搜索失败
        '''
        ele_search = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        search_enabled = ele_search.is_enabled()
        print(ele_search.text)
        print(ele_search.location)
        print(ele_search.size)
        print(ele_search.get_attribute("text"))
        if search_enabled == True:
            ele_search.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']")
            # 判断元素是否可见，用于判定目标元素是否已被查询出来
            print(alibaba_element.get_attribute("displayed"))
            if alibaba_element.get_attribute("displayed") == "true":
                print("搜索成功")
            else:
                print("搜索失败")
    def test_touchaction(self):
        action = TouchAction(self.driver)
        windows_rect = self.driver.get_window_rect()
        print(windows_rect)
        width = windows_rect['width']
        height = windows_rect['height']
        x1 = int(width/2)
        y_start = int(height*4/5)
        y_end = int(height*1/5)
        action.press(x=x1, y=y_start).wait(2000).move_to(x=x1, y=y_end).release().perform()
if __name__ == '__main__':
    pytest.main()