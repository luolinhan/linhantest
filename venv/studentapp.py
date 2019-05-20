# _*_ coding:utf-8 _*_
#Author:lhluo
import requests
import os
import json
import time
import threading
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def reques():
  f = open('log_file.txt', 'a+')
  f.write("7net-studentapp" + '\n')
  headers = {"token": "A44F49F37A8DEAEE60ABDB89FF23C336_WEB_QJTNOB04V05LT4ZL"}
  url = 'http://studentapp.7net.cc/HotMessage/getList?pageIdex=1&pageSize=10'
  r = requests.get(url, headers=headers)
  text = (r.text)
  print ("执行时间：" + time.strftime("%H:%M:%S") + '\n')
  print (url)
  print(text)
  f.write ("time:" + time.strftime("%H:%M:%S") + '\n')
  f.write(url + '\n')
  f.write('Result' + '\n')
  response = json.dumps(text)             
  f.write(response + '\n')

  f.write('===========================================' + '\n')
  f.write('\n')
  f.write('\n')
  f.write('\n')
  url = 'http://studentapp.septnet.cc/HotMessage/getInfo?guid=d12f9b66-5fdf-4769-a37d-183179c41052'
  r = requests.get(url, headers=headers)
  text = (r.text)
  print ("执行时间：" + time.strftime("%H:%M:%S") + '\n')
  print (url)
  print(text)
  f.write ("time:" + time.strftime("%H:%M:%S") + '\n')
  f.write(url + '\n')
  f.write('Result' + '\n')
  response = json.dumps(text)             
  f.write(response + '\n')
  f.write('===========================================' + '\n')
  f.write('\n')
  f.write('\n')
  f.write('\n')
  url = 'http://studentapp.septnet.cc/question/getSubjectList?guid=d12f9b66-5fdf-4769-a37d-183179c41052'
  r = requests.get(url, headers=headers)
  text = (r.text)
  print ("执行时间：" + time.strftime("%H:%M:%S") + '\n')
  print (url)
  print(text)
  f.write ("time:" + time.strftime("%H:%M:%S") + '\n')
  f.write(url + '\n')
  f.write('Result' + '\n')
  response = json.dumps(text)             
  f.write(response + '\n')
  f.write('===========================================' + '\n')
  f.write('\n')
  f.write('\n')
  f.write('\n')
  url = 'http://studentapp.septnet.cc/question/getSubjectInfo?guid=d12f9b66-5fdf-4769-a37d-183179c41052?subject=02'
  r = requests.get(url, headers=headers)
  text = (r.text)
  print ("执行时间：" + time.strftime("%H:%M:%S") + '\n')
  print (url)
  print(text)
  f.write ("time:" + time.strftime("%H:%M:%S") + '\n')
  f.write(url + '\n')
  f.write('Result' + '\n')
  response = json.dumps(text)             
  f.write(response + '\n')
  f.write('===========================================' + '\n')
  f.write('\n')
  f.write('\n')
  f.write('\n')
  url = 'http://studentapp.septnet.cc/userinfo/isBuyExamReport'
  r = requests.post(url, headers=headers)
  text = (r.text)
  print ("执行时间：" + time.strftime("%H:%M:%S") + '\n')
  print (url)
  print(text)
  f.write ("time:" + time.strftime("%H:%M:%S") + '\n')
  f.write(url + '\n')
  f.write('Result' + '\n')
  response = json.dumps(text)             
  f.write(response + '\n')
  f.write('===========================================' + '\n')
  f.write('\n')
  f.write('\n')
  f.write('\n')
  url = 'http://studentapp.septnet.cc/question/getThs?guid=d12f9b66-5fdf-4769-a37d-183179c41052&subject=2'
  r = requests.get(url, headers=headers)
  text = (r.text)
  print ("执行时间：" + time.strftime("%H:%M:%S") + '\n')
  print (url)
  print(text)
  f.write ("time:" + time.strftime("%H:%M:%S") + '\n')
  f.write(url + '\n')
  f.write('Result' + '\n')
  response = json.dumps(text)             
  f.write(response + '\n')
  f.write('===========================================' + '\n')
  f.write('\n')
  f.write('\n')
  f.write('\n')
  url = 'http://studentapp.septnet.cc/question/getInfo?guid=d12f9b66-5fdf-4769-a37d-183179c41052&subject=2&th=3'
  r = requests.get(url, headers=headers)
  text = (r.text)
  print ("执行时间：" + time.strftime("%H:%M:%S") + '\n')
  print (url)
  print(text)
  f.write ("time:" + time.strftime("%H:%M:%S") + '\n')
  f.write(url + '\n')
  f.write('Result' + '\n')
  response = json.dumps(text)             
  f.write(response + '\n')
  f.write('===========================================' + '\n')
  f.write('\n')
  f.write('\n')
  f.write('\n')
  url = 'http://studentapp.septnet.cc/question/getImgs?guid=d12f9b66-5fdf-4769-a37d-183179c41052&subject=2'
  r = requests.get(url, headers=headers)
  text = (r.text)
  print ("执行时间：" + time.strftime("%H:%M:%S") + '\n')
  print (url)
  print(text)
  f.write ("time:" + time.strftime("%H:%M:%S") + '\n')
  f.write(url + '\n')
  f.write('Result' + '\n')
  response = json.dumps(text)             
  f.write(response + '\n')
  f.write('===========================================' + '\n')
  f.write('\n')
  f.write('\n')
  f.write('\n')
  url = 'http://studentapp.septnet.cc/index/kefu'
  r = requests.get(url, headers=headers)
  text = (r.text)
  print ("执行时间：" + time.strftime("%H:%M:%S") + '\n')
  print (url)
  print(text)
  f.write ("time:" + time.strftime("%H:%M:%S") + '\n')
  f.write(url + '\n')
  f.write('Result' + '\n')
  response = json.dumps(text)             
  f.write(response + '\n')
threads=[] 
#多线程
for i in range(1):
    t=threading.Thread(target=reques,args=()) 
    threads.append(t)  
if __name__ == '__main__':
    for i in threads:  
        i.start()  
    for i in threads:  
        i.join()
'''
mail_host="smtp.exmail.qq.com"  
mail_user="linhan@7net.cc"    
mail_pass="Zxsoft00#"   
sender = 'linhan@7net.cc';'xiaojun@7net.cc';'tannuo@7net.cc';'zhangling@7net.cc'
receivers = ['linhan@7net.cc']  

file = open('log_file.txt', 'r') 
js = file.read()
message = MIMEText(js,"plain",'utf-8')
message['From'] = Header("七天教育接口测试", 'utf-8')
message['To'] =  Header("罗林汉", 'utf-8')
subject = '接口测试-学生APP紧急上线'
message['Subject'] = Header(subject, 'utf-8')
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件已发送")
except smtplib.SMTPException:
    print ("Error: 邮件发送失败")'''
