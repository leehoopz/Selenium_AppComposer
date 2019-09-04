# -*- coding: UTF-8 -*-
import unittest
import time
from selenium import webdriver
from time import sleep
import data_config
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        #self.base_url = "http://192.168.0.11:8081"
        self.base_url = data_config.data_base_url
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        print(EC.title_contains("Application Composer"))

    def tearDown(self):
        print("测试结束")
        self.driver.close()
        pass

    def test_login(self):
        u"用户登陆测试"
        print("用户登陆")
        driver = self.driver
        username_box= driver.find_element_by_xpath(data_config.username_xpath)
        password_box= driver.find_element_by_xpath(data_config.password_xpath)
        sleep(2)
        print(username_box.get_attribute("placeholder"))
        username_box.send_keys(data_config.data_username)
        print(username_box.get_attribute("value"))
        password_box.send_keys(data_config.data_password)
        login_button= driver.find_element_by_css_selector(".login-form-button")
        login_button.click()

if __name__ == '__main__':
       unittest.main()
