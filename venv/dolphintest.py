#-*- coding:utf-8 -*-
#Author:lhluo
import requests
import time
import json
import os
import pymysql

f = open('log_file_dolphin.txt', 'a+')
print("创建用户")
def modifyuser():
  url='http://106.12.21.43:5002/api/User/Create'
  s = json.dumps({
      "name": "罗林汉",
      "nickName": "林汉",
      "phone": "13739247505",
      "effectiveTime": "2019-06-23T02:09:48.933Z"
  })
  r=requests.post(url,data=s,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",'Content-Type':'application/json'})
  print(url)
  text=(r.text)
  print(text)
  print (r.status_code)
  print (time.strftime("%H:%M:%S") + '\n')
  f.write ("time:" + time.strftime("%H:%M:%S") + '\n')
  f.write("创建用户" + '\n')
  f.write(url + '\n')
  f.write('传入参数：')
  f.write(s.encode('utf-8').decode("unicode_escape")+ '\n')
  f.write('测试结果：')
  response = json.dumps(text)             
  f.write(response.encode('utf-8').decode("unicode_escape") + '\n')
  f.write('=============================================='+ '\n')
modifyuser()

print("登录")
def login():
  url='http://106.12.21.43:5002/api/Login'
  s = json.dumps({
    "phone": "13739247505",
    "password": "123456"
  })
  r=requests.post(url,data=s,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",'Content-Type':'application/json'})
  print(url)
  text=(r.text)
  print(text)
  print (r.status_code)
  print (time.strftime("%H:%M:%S") + '\n')
  f.write ("time:" + time.strftime("%H:%M:%S") + '\n')
  f.write("登录" + '\n')
  f.write(url + '\n')
  f.write('传入参数：')
  f.write(s.encode('utf-8').decode("unicode_escape")+ '\n')
  f.write('测试结果：')
  response = json.dumps(text)             
  f.write(response.encode('utf-8').decode("unicode_escape") + '\n')
  f.write('=============================================='+ '\n')
login()

print("编辑用户信息")
def edit():
  url='http://106.12.21.43:5002/api/User/Modify'
  s = json.dumps({
  "name": "罗林汉",
  "nickName": "林汉",
  "gender": 1,
  "birthday": "2019-06-23T02:17:34.950Z",
  "province": "安徽",
  "city": "合肥",
  "county": "中国",
  "area": "新站区",
  "address": "临泉路",
  "id": "bbb698e2-dbf0-4bcf-be63-0b12bc118fe0"
})
  r=requests.post(url,data=s,headers={'Content-Type':'application/json'})
  print(url)
  text=(r.text)
  print(text)
  print (r.status_code)
  print (time.strftime("%H:%M:%S") + '\n')
  f.write("编辑用户信息" + '\n')
  f.write(url + '\n')
  f.write('传入参数：')
  f.write(s.encode('utf-8').decode("unicode_escape")+ '\n')
  f.write('测试结果：')
  response = json.dumps(text)             
  f.write(response.encode('utf-8').decode("unicode_escape") + '\n')
  f.write('=============================================='+ '\n')
edit()

print("修改用户密码")
def password():
  url='http://106.12.21.43:5002/api/User/ModifyPassWord'
  s = json.dumps({
  "oldPassWord": "247505",
  "passWord": "123456",
  "confirmPassWord": "123456",
  "id": "bbb698e2-dbf0-4bcf-be63-0b12bc118fe0"
})
  r=requests.post(url,data=s,headers={'Content-Type':'application/json'})
  print(url)
  text=(r.text)
  print(text)
  print (r.status_code)
  print (time.strftime("%H:%M:%S") + '\n')
  f.write("修改用户密码" + '\n')
  f.write(url + '\n')
  f.write('传入参数：')
  f.write(s.encode('utf-8').decode("unicode_escape")+ '\n')
  f.write('测试结果：')
  response = json.dumps(text)
  f.write(response.encode('utf-8').decode("unicode_escape") + '\n')
  f.write('=============================================='+ '\n')
password()

print("修改账户有效期")
def ModifyEffectiveTime():
  url='http://106.12.21.43:5002/api/User/ModifyEffectiveTime'
  s = json.dumps({
  "effectiveTime": "2019-06-22T02:34:25.226Z",
  "id": "bbb698e2-dbf0-4bcf-be63-0b12bc118fe0"
})
  r=requests.post(url,data=s,headers={'Content-Type':'application/json'})
  print(url)
  text=(r.text)
  print(text)
  print (r.status_code)
  print (time.strftime("%H:%M:%S") + '\n')
  f.write("修改账户有效期" + '\n')
  f.write(url + '\n')
  f.write('传入参数：')
  f.write(s.encode('utf-8').decode("unicode_escape")+ '\n')
  f.write('测试结果：')
  response = json.dumps(text)             
  f.write(response.encode('utf-8').decode("unicode_escape") + '\n')
  f.write('=============================================='+'\n')
ModifyEffectiveTime()

print("获取用户信息")
def GetUser():
  url='http://106.12.21.43:5002/api/User/GetUser?id=bbb698e2-dbf0-4bcf-be63-0b12bc118fe0'
  r=requests.get(url,headers={'Content-Type':'application/json'})
  print(url)
  text=(r.text)
  print(text)
  print (r.status_code)
  print (time.strftime("%H:%M:%S") + '\n')
  f.write("获取用户信息" + '\n')
  f.write(url + '\n')
  f.write('传入参数：')
  f.write("id=bbb698e2-dbf0-4bcf-be63-0b12bc118fe0"+ '\n')
  f.write('测试结果：')
  response = json.dumps(text)             
  f.write(response.encode('utf-8').decode("unicode_escape") + '\n')
  f.write('=============================================='+ '\n')
GetUser()

print("获取用户详细信息")
def GetUserDetail():
  url='http://106.12.21.43:5002/api/User/GetUserDetail?id=bbb698e2-dbf0-4bcf-be63-0b12bc118fe0'
  r=requests.get(url,headers={'Content-Type':'application/json'})
  print(url)
  text=(r.text)
  print(text)
  print (r.status_code)
  print (time.strftime("%H:%M:%S") + '\n')
  f.write("获取用户详细信息" + '\n')
  f.write(url + '\n')
  f.write('传入参数：')
  f.write("id=bbb698e2-dbf0-4bcf-be63-0b12bc118fe0"+ '\n')
  f.write('测试结果：')
  response = json.dumps(text)             
  f.write(response.encode('utf-8').decode("unicode_escape") + '\n')
  f.write('=============================================='+ '\n')
GetUserDetail()




