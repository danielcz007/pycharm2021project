# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 22:36
# @Author  : Daniel
from time import ctime, sleep, time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''
显示等待WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))

其中：driver-浏览器驱动

         Timeout:最长超市，默认以秒为单位 

          Poll_frequency:检测间隔的（步长）时间，默认为0.5s

          Ignored_exceptions:超时后的异常，默认情况下抛出NoSuchElementException

          WebDriverWait一般与until()与until_not()方法配合使用

'''
def wb_1():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw')
    element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
    element.send_keys("python")
    sleep(2)
    driver.quit()

''''''
#implicitly_wait隐式等待
#判断某元素，如果超过10s未发现，则抛出异常
#如果在5s内发现，则对该元素进行操作
'''
def wb_3():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)#设置隐式等待最长时间10s
    driver.get('http://www.baidu.com')
    try:
        print(ctime())
        driver.find_element_by_id('k1w').send_keys("python")
        driver.find_element_by_id('su').click()
        sleep(2) #固定休眠时间，等待xx秒
    except NoSuchElementException  as e:
        print(e)
    finally:
        print(ctime())
        driver.quit()
'''
wb_1()
#wb_3()