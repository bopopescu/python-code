import execjs
import requests
import json
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "40",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "_gscu_2116842793=389615802hdkze57; _gscbrs_2116842793=1; Hm_lvt_d2caefee2de09b8a6ea438d74fd98db2=1538961580; ASP.NET_SessionId=rvjjcq0lq41gqsrphevulxqd; Hm_lpvt_d2caefee2de09b8a6ea438d74fd98db2=1538988174; vjkl5=a8289f8999ff4e57810148185fad76048086c78b",
    "Host": "wenshu.court.gov.cn",
    "Origin": "http://oldwenshu.court.gov.cn/",
    "Referer": "http://oldwenshu.court.gov.cn//list/list/?sorttype=1&number=&guid=690f1e5d-fc1b-c74024a3-b1c2ed7f4032&conditions=searchWord+QWJS+++%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2:%E5%A4%A7%E8%BF%9E%20%E4%B8%9C%E8%BD%AF",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    "X-Requested-With": "XMLHttpRequest"
}


def get_guid():
    ctx = execjs.compile("""
            var createGuid = function () {
            return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
            }
            function aa(){
                return createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid();;
            }
    """)
    func = ctx.call("aa")
    return func


def get_number():
    guid = get_guid()
    url = 'http://oldwenshu.court.gov.cn//ValiCode/GetCode'
    data = {'guid': guid}
    res = requests.post(url, headers=headers, data=data)
    return res.text.strip()
def getvlx5():
    with open('getkey.js') as fp:
        js = fp.read()
        ctx = execjs.compile(js)
        vl5x = ctx.call("getKey", "a3e88e89affa632c001fc18bb990d3c02eaf9c7d")
        return vl5x
def postUrl():
    guid = get_guid()
    print(guid)
    vl5x=getvlx5()
    print(vl5x)
    payload = {'Param': '案件类型:刑事案件', 'Index': '1','Page': '10', 'Order': '法院层级','Direction': 'asc', 'vl5x': vl5x, 'guid': guid}
    res=requests.post("http://oldwenshu.court.gov.cn/List/ListContent",data=payload,headers=headers)
    print(res.text)
postUrl()
# print(get_number())
# print(getvlx5())