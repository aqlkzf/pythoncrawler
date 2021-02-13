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
    savepath=r"豆瓣电影top250.xls"
    datalist=getData(baseurl)
    saveData(datalist,savepath)
    #askurl("https://movie.douban.com/top250?start=")
    #print(getData(baseurl))
    print("爬取完毕！")


#全局变量
#影片详情链接的规则
findlink=re.compile(r'<a href="(.*?)">')       #创建正则表达式对象，表示规则（字符串的模式）
#影片图片的链接
findImgSrc=re.compile(r'<img.*src="(.*?)"/>',re.S)   #re.s 忽略换行，让换行符包含在字符中
#影片的片名
findtitle=re.compile(r'<span class="title">(.*?)</span>')
#影片的评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#找到评价人数
#<span>2272079人评价</span>
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq=re.compile(r'<span class="inq">(.*?)</span>')
#找到影片的相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)     #re.S 忽视换行


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
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):#查找需要的字符串，行成列表
        #print(item)  #测试  ，查看电影item所有信息
            data=[]  #保存一部电影所有信息
            item=str(item)
            #获取到影片详情的链接
            # print(item)
            # break
            link=re.findall(findlink,item) [0]  #re库通过正则表达式查找指定的字符串
            data.append(link)
            #print(link)
            imgSrc=re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            titles=re.findall(findtitle,item) #片名可能只有一个中文名，无外文
            if(len(titles)>=2):
                ctitle=titles[0]
                data.append(ctitle)
                otitle=titles[1].replace("/","") # 去掉无关的符号？
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('  ')   #留空
            rating=re.findall(findRating,item)[0]
            data.append(rating)
            judge=re.findall(findJudge,item)[0]
            data.append(judge)
            inq=re.findall(findInq,item)
            if(len(inq)!=0):
                inq=inq[0].replace("。",',')  #去掉句号
                data.append(inq)
            else:
                data.append('  ')
            bd=re.findall(findBd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?',' ',bd)
            bd=re.sub('/'," ",bd)
            data.append(bd.strip())    #去掉前后的空格
            data.append(bd)

            datalist.append(data)
    #print(datalist)
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
        #print(html)
    except urllib.error.URLError as e:
        if hasatter(e,"code"):
            print(e.code)
        if hasatter(e,"reason"):
            print(e.reason)
    return html





#保存数据
def saveData(datalist,savepath):
    wookbook = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    worksheet = wookbook.add_sheet("豆瓣电影TOP250",cell_overwrite_ok=True)  # 创建工作表

    col=('电影详情链接','图片链接','影片中文名','影片外国名','评分','评价数','概况','相关信息')
    for i in range(0,8):
        worksheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])


    wookbook.save("豆瓣电影TOP250.xls")



if __name__ =="__main__":   #当程序执行时
    #调用函数
    main()
   #askurl("https://movie.douban.com/top250?start=")



