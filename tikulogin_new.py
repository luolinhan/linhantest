from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
import sys
sys.path.append("..")
import logging
import logging.config
import time
import json
import re
import random
import traceback
import yaml
import string
import io
from email.mime.text import MIMEText
from email.header import Header
from threading import Timer
import time
import smtplib
import requests
import os

class ImtTestTool():
    def __init__(self):
        # 判断同级目录是否有log文件夹
        isExists = os.path.exists('log')                                              
        if not isExists:
            os.makedirs('log')

        self.init_log(default_path="logging.yaml")
        self.logger = logging.getLogger("imtLogger")

        self.config_init()
        while True:
            self.qamonitor()

    def init_log(self,default_path="logging.yaml",default_level = logging.INFO,env_key = "LOG_CFG"):
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, "r", encoding='utf-8') as f:
                logging.config.dictConfig(yaml.load(f))
        else:
            logging.basicConfig(level=default_level)

    # 接口
    def qamonitor(self):
        f = open('log_file10.txt', 'w')
        headers = {"Content-Type": "application/json"}
        s = json.dumps({"userCode": self.userCode, "userPass": self.userPass})
        url = self.url
        r = requests.post(url, data=s, headers=headers)
        text = (r.text)
        self.logger.info(" 执行时间：" + str(time.strftime("%H:%M:%S")))
        self.logger.info(" url is :{}".format(str(url)))
        self.logger.info(" text receive is :{}".format(str(text)))
        response = json.dumps(text)
        if r.status_code == 200 and eval(text)['message'] == 'success':
            self.logger.info("返回正常")
        else:
            self.logger.error("结果异常:{}".format(str(text)))
            f.write("time:" + time.strftime("%H:%M:%S") + '\n')
            f.write('\n')
            f.write(url)
            f.write('\n')
            f.write("请求异常!!!message is "  + eval(text)['message'])
            f.write('\n')
            f.write(json.dumps(text))
            f.write('\n')
            f.close()
            timer_interval = 1
            def delayrun():
                self.logger.info('doing')
            t = Timer(timer_interval, delayrun)
            t.start()
            while True:
                time.sleep(5)
                self.qamail()
                sys.exit()
        f.write('\n')


    # 发送邮件
    def qamail(self):
        file = open('log_file10.txt', 'r')
        js = file.read()
        message = MIMEText(js, "plain", 'utf-8')
        message['From'] = Header("七天教育自动化测试", 'utf-8')
        message['To'] = Header("罗林汉", 'utf-8')
        subject = '自动化测试-重要接口监控'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers.split(";"), message.as_string())
            self.logger.info("邮件发送成功, 接受者有：{}".format(str(self.receivers)))
        except smtplib.SMTPException:
            self.logger.error("Error: 无法发送邮件:{}".format(str(message)))

    # 配置文件读取
    def config_init(self):
        config_file = os.path.dirname(os.path.realpath(__file__)) + '/tikulogin.yaml'
        f = io.open(config_file, 'r', encoding='utf-8')
        cont = f.read()
        configs = yaml.load(cont)
        config = configs.get('root')
        self.logger.info(config)

        self.mail_host = config['mail.config']['mail_host']
        self.mail_user = config['mail.config']['mail_user']
        self.mail_pass = config['mail.config']['mail_pass']
        self.sender = config['mail.config']['sender']
        self.receivers = config['mail.config']['receivers']

        self.userCode = config['param.config']['userCode']
        self.userPass = config['param.config']['userPass']
        self.url = config['param.config']['url']
       

        f.close()

if __name__ == '__main__':
    imt = ImtTestTool()
