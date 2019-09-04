import unittest
import time
from selenium import webdriver
from time import sleep
import data_config
import webapp_login
from selenium.webdriver.common.action_chains import ActionChains

class CreateProjectTestCase(unittest.TestCase):
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

    def test_create_project(self):
        u"创建工程"
        webapp_login.LoginTestCase.test_login(self)
        print("创建工程")
        driver =self.driver
        create_button = driver.find_element_by_css_selector("div.menu-button:nth-child(3) > div:nth-child(2)")
        create_button.click()
        project_name_box =driver.find_element_by_css_selector("input.ant-input")
        sleep(2)
        project_name_box.clear()
        project_name_box.send_keys("project_name01")
        project_description_box=driver.find_element_by_css_selector("textarea.ant-input")
        project_description_box.clear()
        project_description_box.send_keys("project_description01")

        project_save_button=driver.find_element_by_css_selector("div.hover-btn:nth-child(1)")
        project_save_button.click()
        sleep(2)


if __name__ == '__main__':
       unittest.main()


