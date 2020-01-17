# from bs4 import BeautifulSoup
# import requests
# url='http://oldwenshu.court.gov.cn/list/list/?sorttype=1&number=&guid=ae67137d-070c-9d0218c5-24af600c5f08&conditions=searchWord+QWJS+++%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2:%E8%80%90%E5%85%8B'
# # data = {'number':'FcOOwrcBAzEMw4DDgMKVwpjDhFAyw64/wpLDnw3DmkPCncOSw7NgFnLCqcK8Z8Kkw5gVwpvCncOmwonDt8O2wpHDtSx+KcK1KnbDlnXCt0DDtXpjwqAswoLDgMKwOk7DggfDo8OcwpjCkCvCtMOCEMOJwqgCw4fDsjHDh8OvECp4FMKCwqLDk8OVwoHCrwF9asKiwqnCjQcCw5xfwo7Cl17CvsOBw7TDlG4Yw4TChsOmb8OEfCAvScK1w4EWLsO4w67Cj8OIN8OgwrvDgSUEwoIsw7kD'}
# rt = requests.get(url)
# rt.encoding='utf-8'
# print(str(rt.text))
# sp = BeautifulSoup(str(rt.text),"html.parser")
# print(sp.select('span_datacount'))
# for y in range(len(sp.select('a'))):
#     print(sp.select('a')[y].text)
#     from PyExecJs
#
# import reimport execjs
# # with open('getkey.js') as fp:
# #     js = fp.read()
# #     ect = execjs.compile(js)
# #     vl5x = ect.call('getguid')
# #     print(vl5x)
# #
import requests
from bs4 import BeautifulSoup
import json
def GetCookie():
    s=requests.session()
    loginUrl='https://hu60.cn/q.php/user.login.html?u=index.index.html'
    postData={
        'type': 1,
    'name': 'wapjin',
    'pass': 123456,
    'go': '登录'
    }
    rs=s.post(loginUrl,postData)
    c=requests.cookies.RequestsCookieJar()#利用RequestsCookieJar获取
    c.set('cookie-name','cookie-value')
    s.cookies.update(c)
    return s.cookies.get_dict()
def Get(gg):
    s=requests.session()
    cookies1 = GetCookie()['hu60_sid']
    url = 'https://hu60.cn/q.php/addin.chat.公共聊天室.html'
    postData={
        'content':gg,
        'token': '31f7a1e9e62fdb52e1b80e4fa4544996',
            'go': '快速发言'
    }
    rs=s.post(url,postData)
    print(rs.text)
headers = {
    'Content-Type': 'application/json;charset=utf-8',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"

}
data = {
'pass': '111.2.19.13'
}
#     data = json.dumps(data)
s = requests.session()
cookies1 = GetCookie()['hu60_sid']
url = 'https://hu60.cn/q.php/'+cookies1+'/addin.chat.公共聊天室.html'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
cookies = GetCookie()  # 这里就是利用上面的函数获得的Cookies
rs = s.get(url, headers=headers, cookies=cookies, verify=True)
rs.encoding = 'utf-8'
# print(rs.text)
sp = BeautifulSoup(str(rs.text),"html.parser")
# print(sp.select('.chat-list')[0].text)
arr =[]
for i in sp.select('.chat-list'):
    arr.append(i.text.replace("\n", ",").split(','))
for x in arr:
    for t in range(x.count('')):
        x.remove('')

Get(arr[0])
