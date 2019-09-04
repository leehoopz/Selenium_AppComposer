import unittest
import time
from selenium import webdriver
from time import sleep
import data_config
import webapp_login
from selenium.webdriver.common.action_chains import ActionChains

class DeleteProjectTestCase(unittest.TestCase):
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

    def test_delete_project(self):
        u"删除工程"
        webapp_login.LoginTestCase.test_login(self)
        print("删除工程")
        driver =self.driver
        project_list_01 = driver.find_element_by_css_selector(data_config.project_list_01_css_selector)
        ActionChains(driver).move_to_element(project_list_01).perform()
        sleep(2)
        project_config_button = driver.find_element_by_css_selector(data_config.project_config_button_css_selector)
        project_config_button.click()
        project_delete_botton =driver.find_element_by_css_selector(data_config.project_delete_button_css_selector)
        project_delete_botton.click()
        project_delete_confirm_yes =driver.find_element_by_css_selector(".ant-spin-container")
        project_delete_confirm_yes.click()
        sleep(3)

if __name__ == '__main__':
       unittest.main()


