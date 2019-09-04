# -*- coding: UTF-8 -*-
import unittest
import time
from selenium import webdriver
from time import sleep
import data_config
from selenium.webdriver.common.action_chains import ActionChains

class LogoutTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        #self.base_url = "http://192.168.0.11:8081"
        self.base_url = data_config.data_base_url
        self.driver.get(self.base_url)

    def tearDown(self):
        print("测试结束")
        self.driver.close()
        pass

    def test_logout(self):
        u"用户登出测试"
        print("用户登陆")
        driver = self.driver
        username_box= driver.find_element_by_xpath(data_config.username_xpath)
        password_box= driver.find_element_by_xpath(data_config.password_xpath)
        sleep(2)
        username_box.send_keys(data_config.data_username)
        password_box.send_keys(data_config.data_password)
        login_button= driver.find_element_by_css_selector(".login-form-button")
        login_button.click()

        userconfig = driver.find_element_by_css_selector("div.ant-dropdown-trigger > span:nth-child(2)")
        ActionChains(driver).move_to_element(userconfig).perform()
        sleep(2)
        print("切换至config")
        print("用户登出")
        #logout_button = driver.find_element_by_link_text("Logout")
        #logout_button =driver.find_element_by_name("Logout")
        #logout_button =driver.find_element("Logout")
        #logout_button =driver.find_element_by_tag_name("Logout")
        #logout_button =driver.find_element_by_class_name("Logout")
        logout_button =driver.find_element_by_xpath("//*[@id='cdk-overlay-1']/div/div/ul/li[2]")
        logout_button.click()

if __name__ == '__main__':
       unittest.main()
