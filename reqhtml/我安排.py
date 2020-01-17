#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-21 11:17
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : 我安排.py
from wsgiref.simple_server import make_server
import json
# 导入我们自己编写的application函数:
def geturl(datas,name):
    arr = []
    for i in datas:
        arr.append(str(i)[:int(i.index("="))])
        arr.append(str(i)[int(i.index("=")) + 1:])

    print(arr)
    getdata = {}
    for i in range(0, len(arr), 2):
        getdata[arr[i]] = arr[i + 1]

    return getdata[name]
urls={
    "":"index",
    "api":"api"

}
def index(datas):
    return "ok server"
def api(datas):


# # datas = str(environ['QUERY_STRING'])

    r= geturl(datas,'u')
    r1 = geturl(datas, 'y')
    data = {

        'code': 1,
        'msg': "公司",
        'data':r,
        'data2': r1

    }
    req= json.dumps(data,ensure_ascii=False)
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/json;charset=utf-8')])
    url = environ['PATH_INFO'][1:]
    datas = str(environ['QUERY_STRING']).split('&')
    if url in urls:
        data = urls[url](datas)

    return [data.encode()]
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

# {'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'ZK3JI8EY23R8ITM', 'COMSPEC': 'C:\\windows\\system32\\cmd.exe', 'FP_NO_HOST_CHECK': 'NO', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Administrator', 'LIB': 'C:\\Program Files\\SQLXML 4.0\\bin\\', 'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local', 'LOGONSERVER': '\\\\ZK3JI8EY23R8ITM', 'NUMBER_OF_PROCESSORS': '2', 'OS': 'Windows_NT', 'PATH': 'C:\\windows\\system32;C:\\windows;C:\\windows\\System32\\Wbem;C:\\windows\\System32\\WindowsPowerShell\\v1.0\\;d:\\u8c\\admin;C:\\Program Files (x86)\\Microsoft SQL Server\\80\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\90\\Tools\\binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\90\\Tools\\binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\90\\DTS\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\90\\Tools\\Binn\\VSShell\\Common7\\IDE\\;C:\\Program Files (x86)\\Microsoft Visual Studio 8\\Common7\\IDE\\PrivateAssemblies\\;D:\\nojs\\;C:\\Program Files\\PuTTY\\;D:\\py;D:\\py\\Scripts;C:\\Program Files (x86)\\ZeroTier\\One\\;C:\\Program Files (x86)\\Smart Projects\\IsoBuster;D:\\py\\Scripts;D:\\py\\;C:\\Users\\Administrator\\AppData\\Roaming\\npm;D:\\nojs;D:\\MinGW\\bin;D:\\sql3;D:\\py\\Scripts', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'AMD64 Family 21 Model 48 Stepping 1, AuthenticAMD', 'PROCESSOR_LEVEL': '21', 'PROCESSOR_REVISION': '3001', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM': 'D:\\PyCharm 2019.1.3\\bin;', 'PYCHARM_DISPLAY_PORT': '59251', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'D:\\python code\\reqhtml;D:\\PyCharm 2019.1.3\\helpers\\pycharm_matplotlib_backend;D:\\PyCharm 2019.1.3\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\windows', 'TEMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'USERDOMAIN': 'ZK3JI8EY23R8ITM', 'USERNAME': 'Administrator', 'USERPROFILE': 'C:\\Users\\Administrator', 'WINDIR': 'C:\\windows', 'WINDOWS_TRACING_FLAGS': '3', 'WINDOWS_TRACING_LOGFILE': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log', '_DFX_INSTALL_UNSIGNED_DRIVER': '1', 'SERVER_NAME': 'ZK3JI8EY23R8ITM', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/index', 'QUERY_STRING': 'apge=1', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': '127.0.0.1:8000', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36', 'HTTP_SEC_FETCH_USER': '?1', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'HTTP_SEC_FETCH_SITE': 'none', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9,en;q=0.8', 'wsgi.input': <_io.BufferedReader name=140>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}
