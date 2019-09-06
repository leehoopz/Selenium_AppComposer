#coding=utf-8
import unittest
import HTMLTestRunner
import webapp_login,webapp_logout,webapp_create_project,webapp_delete_project
import time
from log.user_log import UserLog

def creat_suite():
    #print("创建测试套")
    suite= unittest.TestSuite()
    suite.addTest(unittest.makeSuite(webapp_login.LoginTestCase))
    suite.addTest(unittest.makeSuite(webapp_logout.LogoutTestCase))
    suite.addTest(unittest.makeSuite(webapp_create_project.CreateProjectTestCase))
    suite.addTest(unittest.makeSuite(webapp_delete_project.DeleteProjectTestCase))

    return suite

if __name__ =='__main__':
    suite = creat_suite()
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    print(file_prefix)
    fp = open("./Report/" + file_prefix + "_result.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"Robot测试报告", description=u"测试用例执行情况",verbosity=2)
    runner.run(suite)
    fp.close()