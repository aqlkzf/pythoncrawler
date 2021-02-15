# -*- coding = utf-8 -*-
# @Time : 2021-02-14 18:03
# @Author : QianLiKuaiZaiFeng
# @File : testsqlite.py
# @Software : PyCharm


import sqlite3
conn=sqlite3.connect("test.db")          #打开或创建数据库文件
print("Opened database successfully")