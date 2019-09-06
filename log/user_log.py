# coding =utf-8
import logging
import os
import datetime

class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # 日志文件命名
        base_dir=os.path.dirname(os.path.abspath(__file__))
        log_dir=os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name =log_dir+"/"+log_file
        print(log_name)

        #控制台输出日志
        consle=logging.StreamHandler()
        self.logger.addHandler(consle)
        #logger.debug("consleinfo")

        #文件输出日志
        #file_handle=logging.FileHandler("D:\\MyProject\\Python\\Selenium_AppComposer\\log\\logs\\test.log")
        self.file_handle=logging.FileHandler(log_name,'a',encoding='utf-8')
        formatter =logging.Formatter('%(asctime)s %(filename)s --> %(funcName)s %(levelno)s: %(levelname)s --> %(message)s')
        self.file_handle.setFormatter(formatter)

        self.logger.addHandler(self.file_handle)
        self.logger.debug("testlog_output")


    def get_log(self):
        return self.logger

    def close_log(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)