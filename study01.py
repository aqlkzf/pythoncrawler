# -*- coding = utf-8 -*-
# @Time : 2021-02-10 14:50
# @Author : QianLiKuaiZaiFeng
# @File : study01.py.py
# @Software : PyCharm

import sys
import  re   #正则表达式 ，文字匹配
import urllib.request #制定url，获取网页数据
import urllib.error
import xlwt  #excel操作
from bs4 import BeautifulSoup   #网页解析，获取数据
import sqlite3  #进行SQLLite数据库操作
def main():
    baseurl="https://movie.douban.com/top250?start="
    # savepath=r"./豆瓣电影top250.xls"
    # datalist=getData(baseurl)
    # saveData(savepath)
    #askurl("https://movie.douban.com/top250?start=")
    print(getData(baseurl))


#爬取网页
#解析数据
#保存数据

#爬取网页
def getData(baseurl):
    datalist=[]

    for i in range(0,10):
        url=baseurl+str(i*25)
        #datalist.append(askurl(url))
        html=askurl(url)  #保存获取到的网页源码
    #逐一解析
    return datalist


#得到指定url的网页信息
def askurl(url):
    #head用户代理 表示告诉豆瓣服务器 我们是什么类型的浏览器   ，本质告诉服务器我们可以接受什么水平的数据
    #模拟浏览器头部信息 向豆瓣服务器发送消息
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
    request = urllib.request.Request(url, headers=head)

    try:
        response  = urllib.request.urlopen(request)
        html=response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasatter(e,"code"):
            print(e.code)
        if hasatter(e,"reason"):
            print(e.reason)
    return html





#保存数据
def saveData(savepath):
    pass


if __name__ =="__main__":   #当程序执行时
    #调用函数
    main()
   #askurl("https://movie.douban.com/top250?start=")
