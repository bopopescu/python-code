#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-20 9:33
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : tuan.py
from bs4 import BeautifulSoup
import requests
import xlwt
import time
def Getcook():
    s = requests.session()
    url = 'http://wcphp172.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/index.php?password=xinhai0574'
    res = s.get(url)
    c = requests.cookies.RequestsCookieJar()
    # c.set('PHPSESSID', 'l5vq1hvgh5qtlnvhsfs630fna4')
    s.cookies.update(c)
    return s.cookies.get_dict()

# http://wcphp172.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/order.php?xh_name=&xh_status=

def lookurlo():
    s= requests.session()
    cookies = Getcook()
    # print(cookies)
    url = 'http://wcphp172.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/order.php?xh_name=&xh_status='  # 这里的URL就是通过开发者工具找到的网页的请求信息里的Request URL
    res = s.get(url, cookies=cookies, verify=True,)
    res.encoding='utf-8'
    soup = BeautifulSoup(str(res.text), 'html.parser', from_encoding='utf-8')
    # print(soup.select('tbody')[0].select('tr')[0].text.replace("\n", ","))
    # print(soup.select('.rows')[0].text[2:4])
    arr1=[]
    result = soup.select('thead')[0].select('tr')[0].text.replace("\n", ",").split(',')
    arr1.append(result)

    for ty in range(int(soup.select('.end')[0].text)+1):
        if ty>0:
            url1 = 'http://wcphp172.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/order.php?xh_name=&xh_status=&page='+str(ty)

            res1 = s.get(url1,cookies=cookies, verify=True,)  # requests后面的方法要根据网页的请求信息来判断
            res1.encoding = 'utf-8'  # 可加可不加，爬虫结果乱码，可以用这个代码更正
            soup1 = BeautifulSoup(str(res1.text), 'html.parser', from_encoding='utf-8')


            for i in soup1.select('tbody'):
                for t in i.select('tr'):
                        arr1.append(t.text.replace("\n", ",").split(','))

    return arr1
def lookurl1():
    arr1 = []
    s= requests.session()
    cookies = Getcook()
    print(cookies)
    url = 'http://wcphp172.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/order.php?xh_name=&xh_status=2'  # 这里的URL就是通过开发者工具找到的网页的请求信息里的Request URL
    res = s.get(url, cookies=cookies, verify=True,)
    res.encoding='utf-8'
    soup = BeautifulSoup(str(res.text), 'html.parser', from_encoding='utf-8')
    result = soup.select('thead')[0].select('tr')[0].text.replace("\n", ",").split(',')
    arr1.append(result)
    # print(soup.select('tbody')[0].select('tr')[0].text.replace("\n", ","))
    shu = soup.select('.rows')[0].text
    row = int(shu[2:int(len(shu)) - 4])
    row2 =int(row)/15
    if row2<0:
        row=0

    for ty in range(row+1):

        if ty>0:
            url1 = 'http://wcphp172.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/order.php?xh_name=&xh_status=2&page='+str(ty)

            res1 = s.get(url1,cookies=cookies, verify=True,)  # requests后面的方法要根据网页的请求信息来判断
            res1.encoding = 'utf-8'  # 可加可不加，爬虫结果乱码，可以用这个代码更正
            soup1 = BeautifulSoup(str(res1.text), 'html.parser', from_encoding='utf-8')


            for i in soup1.select('tbody'):
                for t in i.select('tr'):
                        arr1.append(t.text.replace("\n", ",").split(','))
    for w in arr1:
        for t in range(w.count('')):
            w.remove('')
    return arr1
#
def write_data_to_excel(result,result1):
    # 将sql作为参数传递调用get_data并将结果赋值给result,(result为一个嵌套元组)


    # 实例化一个Workbook()对象(即excel文件)
    wbk = xlwt.Workbook()
    # 建立第一个表格
    # 新建一个名为Sheet1的excel sheet。此处的cell_overwrite_ok =True是为了能对同一个单元格重复操作。
    sheet = wbk.add_sheet('Sheet1',cell_overwrite_ok=True)
    # 获取当前日期，得到一个datetime对象如：(2016, 8, 9, 23, 12, 23, 424000)

    # 遍历result中的没个元素。

    for i in range(len(result)):
        # 对result的每个子元素作遍历，
        for j in range(len(result[i])):
            # 将每一行的每个元素按行号i,列号j,写入到excel中。
            sheet.write(i, j, result[i][j])
    # 建立第二个表格
    sheet = wbk.add_sheet('Sheet2', cell_overwrite_ok=True)
    # 获取当前日期，得到一个datetime对象如：(2016, 8, 9, 23, 12, 23, 424000)

    # 遍历result中的没个元素。

    for i in range(len(result1)):
        # 对result的每个子元素作遍历，
        for j in range(len(result1[i])):
            # 将每一行的每个元素按行号i,列号j,写入到excel中。
            sheet.write(i, j, result1[i][j])

    # 以传递的name+当前日期作为excel名称保存。

    wbk.save('./'+str(str(time.strftime("%Y.%m.%d %H.%M.%S", time.localtime())))+'.xls')
# 生成表格
write_data_to_excel(lookurl1(),lookurlo())
print('ok')
# print(lookurlo())