# -*- coding = utf-8 -*-
# @Time : 2021-02-10 15:30
# @Author : QianLiKuaiZaiFeng
# @File : testurllib.py
# @Software : PyCharm

import urllib.request
#获取一个get 请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  #对获取到的网页源码进行utf-8解码


#获取一个post请求    #http://httpbin.org/
# import urllib.parse
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8')
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))  #对获取到的网页源码进行utf-8解码
#

#
#超时处理
# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=1)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")


# response=urllib.request.urlopen("http://baidu.com",timeout=1)
# #print(response.status)
# print(response.getheader("Server"))


#伪装为浏览器
#url="https://www.douban.com"
# url="http://httpbin.org/post"
# headers={
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
# }
# data=bytes(urllib.parse.urlencode({"name":"eric"}),encoding='utf-8')
# req=urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response=urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

url="https://www.douban.com"
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
 }
req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode('utf-8'))


