# -*- coding: UTF-8 -*-
import unittest
import time
from selenium import webdriver
from time import sleep
import data_config
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import random
from PIL import Image
import pytesseract

driver =webdriver.Firefox()


# #验证元素是否出现时，再执行
# driver.get("http://www.baidu.com")
# time.sleep(2)
# print(EC.title_contains("百度"))
# #等待3s,找到class name为：“s_ipt”才继续
# locator =(By.CLASS_NAME,"s_ipt")
# WebDriverWait(driver,3).until(EC.visibility_of_element_located(locator))

# #生成5个 8位长度 邮箱名
# for i in range(5):
#     user_email="".join(random.sample('123456789abcde',8))+"@163.com"
#     print(user_email)


# 计算验证码：
#x 1.先跳转到验证码页面： driver.get("xxx.com")
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(3)
print(EC.title_contains("注册"))
email_element=driver.find_element_by_id("register_email")
driver.save_screenshot("D:/testshot.png")
#code_element =driver.find_element_by_id("getcode_num")
code_element =driver.find_element_by_css_selector("#getcode_num")
print(code_element.location) #{"x":123,"y":345}
left=code_element.location['x']
top=code_element.location['y']
right=code_element.size['width']+left
height=code_element.size['height']+top
im=Image.open("D:/testshot.png")
img= im.crop((left,top,right,height))
img.save("D:/testshot2.png")


