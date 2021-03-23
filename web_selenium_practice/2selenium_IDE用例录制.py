# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 21:41
# @Author  : Daniel
'''
    selenium IDE 一个基础工具而已，用处不多
    -  下载/安装 国内只能下载火狐  chrome需要翻墙
        https://www.selenium.dev/downloads/
    -   启动IDE
    -   IDE的使用
'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
driver.maximize_window()

# 鼠标悬停至“设置”链接
#driver.find_element_by_link_text('设置').click()
driver.find_element_by_xpath('//*[@id="s-usersetting-top"]').click()
sleep(1)
# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# 搜索结果显示条数
sel = driver.find_element_by_xpath('//*[@name="NR"]').get_attribute('value')
print(sel)
#Select(sel).select_by_value('50')  # 显示50条
# ……

driver.quit()