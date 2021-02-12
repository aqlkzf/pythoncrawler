# -*- coding = utf-8 -*-
# @Time : 2021-02-10 17:47
# @Author : QianLiKuaiZaiFeng
# @File : testbs.py
# @Software : PyCharm

#Tag   标签及其内容
#NavigableString   标签里的string
#BeautifulSoup  表示整个文档
#Comment  特殊的NavigableString 无注释
from bs4 import BeautifulSoup
import  re
file=open("./baidu.html","rb")
html=file.read().decode('utf-8')
bs=BeautifulSoup(html,"html.parser")
# print(bs.title)
# print(bs.a)
#Tag  标签及其内容  ；拿到所找到的第一个内容
#NavigableSting  标签里的内容sting

# print(bs.title.string)
# print(bs.a.attrs)
#
#--------------------------------------------------------------------------------------
#应用
#文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])
#
#
#



#文档的搜索
#find_all    字符串过滤，会查找与字符串完全匹配的内容
#t_list=bs.find_all("a")



#正则表达式搜索
#使用search方法来匹配内容
# import re
# t_list=bs.find_all(re.compile("a"))



#用 方法来搜索  ：传入一个函数 ，根据函数的要求搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list=bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)
# #print(t_list)


#kwargs 参数
#t_list=bs.find_all(id="head")
# t_list=bs.find_all(class_=True)
# for item in t_list:
#     print(item)

#3.text 参数

#t_list=bs.find_all(text="hao123")






#t_list=bs.find_all(text=re.compile("\d"))

#4.limit 参数
# t_list=bs.find_all("a",limit=3)
# for item in t_list:
#      print(item)


#css 选择器


t_list=bs.select('title')

for item in t_list:
    print(item)











