import json
from bs4 import BeautifulSoup
import xlwt
import time
import requests
url = 'http://wcphp172.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/index.php?xh_name=&xh_status=2'
res = requests.get(url)
res.encoding='utf-8'
soup = BeautifulSoup(str(res.text), 'html.parser', from_encoding='utf-8')
# print(soup.select('tbody')[0].select('tr')[0].text.replace("\n", ","))
arr1=[]
result = soup.select('thead')[0].select('tr')[0].text.replace("\n", ",").split(',')
arr1.append(result)
print(soup.select('.rows')[0].text[2:4])
for ty in range(int(soup.select('.rows')[0].text[2:4])+1):
    if ty>0:
        url1 = 'http://wcphp172.xinhaimobile.cn/xh_groupbuy/on-line/xh_shop/admin/index.php?xh_name=&xh_status=2&page='+str(ty)

        res1 = requests.get(url1)
        res1.encoding = 'utf-8'
        soup1 = BeautifulSoup(str(res1.text), 'html.parser', from_encoding='utf-8')


        for i in soup1.select('tbody'):
            for t in i.select('tr'):
                    arr1.append(t.text.replace("\n", ",").replace("[ 发货 ]", "").replace(" ", "").split(','))
# for x in arr:
#     for t in range(x.count('')):
#         x.remove('')

for w in arr1:
    for t in range(w.count('')):
        w.remove('')
# print(list1)
def write_data_to_excel(result1):

    wbk = xlwt.Workbook()



    sheet = wbk.add_sheet('Sheet2', cell_overwrite_ok=True)


    for i in range(len(result1)):

        for j in range(len(result1[i])):

            sheet.write(i, j, result1[i][j])


    wbk.save('./'+str(str(time.strftime("%Y.%m.%d %H.%M.%S", time.localtime())))+'.xls')
write_data_to_excel(arr1)