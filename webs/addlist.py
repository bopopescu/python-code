
import json
from bs4 import BeautifulSoup
import xlwt
import time
import requests
def lookurl():
    url = 'http://wcphp172.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/index.php?xh_name=&xh_status=2'       #这里的URL就是通过开发者工具找到的网页的请求信息里的Request URL
    # url ='http://wcphp12.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/?page=1'
    url2 ='http://wcphp172.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/index.php?xh_name=&xh_status=3&page=1'

    res = requests.get(url)   #requests后面的方法要根据网页的请求信息来判断
    res.encoding='utf-8'      #可加可不加，爬虫结果乱码，可以用这个代码更正
    soup = BeautifulSoup(str(res.text), 'html.parser', from_encoding='utf-8')

    # print(soup.select('tbody')[0].select('tr')[0].text.replace("\n", ","))
    arr1=[]
    arr=[]
    result = soup.select('thead')[0].select('tr')[0].text.replace("\n", ",").split(',')
    arr.append(result)
    res2 = requests.get(url2)   #requests后面的方法要根据网页的请求信息来判断
    res2.encoding='utf-8'      #可加可不加，爬虫结果乱码，可以用这个代码更正
    soup2 = BeautifulSoup(str(res2.text), 'html.parser', from_encoding='utf-8')
    arr1.append(soup2.select('thead')[0].select('tr')[0].text.replace("\n", ",").split(','))
    # print(soup2.select('.end')[0].text)
    for ty in range(int(soup.select('.rows')[0].text[2:4])+1):
        if ty>0:
            url1 = 'http://wcphp172.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/index.php?xh_name=&xh_status=2&page='+str(ty)

            res1 = requests.get(url1)  # requests后面的方法要根据网页的请求信息来判断
            res1.encoding = 'utf-8'  # 可加可不加，爬虫结果乱码，可以用这个代码更正
            soup1 = BeautifulSoup(str(res1.text), 'html.parser', from_encoding='utf-8')


            for i in soup1.select('tbody'):
                for t in i.select('tr'):
                        arr1.append(t.text.replace("\n", ",").replace("[ 发货 ]", "").replace(" ", "").split(','))
    for i in soup.select('tbody'):
        for t in i.select('tr'):
                arr.append(t.text.replace("\n", ",").split(','))
    # for x in arr:
    #     for t in range(x.count('')):
    #         x.remove('')

    for w in arr1:
        for t in range(w.count('')):
            w.remove('')
    for c in arr1:
        for t in range(c.count('>')):
            c.remove('')
    # for r in arr1:
    #     for t in range(r.count('\t')):
    #         t.remove('\t')
    # print(list1)

    # for x in range(len(arr1)):
    #     for y in range(len(arr1[x])):
    #         arr1[x][y].remove('')
    # print(type(arr))

    # print(list1)
    # print(list1)

    # print(arr)


    # print(g)
    # print(type(g))
    return arr1
    # result=soup.select('tbody')[0].text.replace("\n", ",")


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
# write_data_to_excel(arr,arr1)
