
import requests
import json

url = 'http://oldwenshu.court.gov.cn/List/ListContent'

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",


}
# Accept: */*
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
# Connection: keep-alive
# Content-Length: 221
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# Cookie: _gscu_805277408=69473044p6hlsd69; __utma=25640163.410187306.1569561625.1569561625.1569561625.1; __utmz=25640163.1569561625.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gscbrs_805277408=1; Hm_lvt_d2caefee2de09b8a6ea438d74fd98db2=1569561847,1569716305,1570499895; ASP.NET_SessionId=pxhbi0b1n4cipatmuhuonlyd; VCode=d87d39f3-3359-4344-98f2-a73fa73c3a4c; _gscs_805277408=t70507661bnxgkf11|pv:5; Hm_lpvt_d2caefee2de09b8a6ea438d74fd98db2=1570507725; vjkl5=6d2ff04792ff92ab5901c718af6abe0b4b4a4880
# Host: oldwenshu.court.gov.cn
# Origin: http://oldwenshu.court.gov.cn
# Referer: http://oldwenshu.court.gov.cn/list/list/?sorttype=1&number=&guid=34bd057d-0c0b-100341a3-fe3bc55633d4&conditions=searchWord+QWJS+++%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2:%E8%80%90%E5%85%8B
# User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
# X-Requested-With: XMLHttpRequest
data={

'Param': '全文检索:耐克',
'Index': 1,
'Page': 10,
'Order': '法院层级',
'Direction': 'asc',
'vl5x': 'ab930f00b1203477db2036f8',
'guid': '28322370-27ac-4d6fa1f8-b189851cf426',
'number': 'NXLK'

}
data=json.dumps(data)
res = requests.post(url,headers=headers,data=data)
res.encoding='utf-8'
content = json.loads(res.text,encoding='utf-8')
print(content)