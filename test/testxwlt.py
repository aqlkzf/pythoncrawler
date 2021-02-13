# -*- coding = utf-8 -*-
# @Time : 2021-02-14 0:32
# @Author : QianLiKuaiZaiFeng
# @File : testxwlt.py
# @Software : PyCharm

import xlwt

#
# wookbook=xlwt.Workbook(encoding="utf-8")   #创建workbook对象
# worksheet=wookbook.add_sheet("sheet1")    #创建工作表
# worksheet.write(0,0,'hello')
# wookbook.save("student.xls")



wookbook=xlwt.Workbook(encoding="utf-8")   #创建workbook对象
worksheet=wookbook.add_sheet("sheet1")    #创建工作表
for i in range(0,100):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d *  %d= %d"%(i+1,j+1,(i+1)*(j+1)))
wookbook.save("student.xls")