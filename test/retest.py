# -*- coding = utf-8 -*-
# @Time : 2021-02-12 21:37
# @Author : QianLiKuaiZaiFeng
# @File : retest.py
# @Software : PyCharm
#.*@126.com

import re

# #正则表达式   ：字符串模式（判断字符串是否符合一定的标准）
# #创建模式对象
# pat=re.compile("AA")  #此处的AA是正则表达式，用来去验证其它的字符串
#
# m=pat.search('6596gfytfytdfhgujg')  #search方法进行比对 查找
#
# #无模式对象
# m=re.search("asd","Aasd")  #前面的字符串是模板，后面的字符串是被校验的对象
# print(m)+++++

# m=re.findall("a","AFGJIODajijfjfa")  #前面字符串是规则（正则表达式），后面字符串是被校验的字符串
# print(m)

#print(re.findall("[A-Z]","SJIHIHUOJDNENFJUNHFJUjjdfidjfohh"))


print(re.sub("a","A","sfdfhduhfabcdajfdifohhoijioh"))  #在第三个字符串中，找到a 用A来替换
#建议在正则表达式中，被比较的字符串前面加r,不用担心转义字符的问题




