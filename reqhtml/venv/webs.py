#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-20 10:22
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : webs.py
import socket
from pys import getdata
def service_client(new_socket):
    #接受客户端的需求
    request = new_socket.recv(1024)
    head=str(request)[7:8]

    print(head)
    data = {
        'msg': 'ok',
        'data': getdata(int(head)),
        'code': 1

    }
    #回传数据给客户端
    response = 'HTTP/1.1 200 OK\r\n\r\n'
    # response += 'Accept: */*\r\n'
    #
    #
    # response += 'Accept-Encoding: gzip, deflate, br\r\n'
    # response += 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n'
    # response += 'Connection: keep-alive\r\n'
    # response += 'Content-Type: text/html;charset=UTF-8\r\n'
    # response += 'Host: event.csdn.net\r\n'
    # response += 'Origin: https://blog.csdn.net\r\n'
    # response += 'Referer: https://blog.csdn.net/dcclient/article/details/91351785\r\n'
    # response += 'Sec-Fetch-Mode: cors\r\n'
    # response += 'Sec-Fetch-Site: same-site\r\n'
    # response += 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36\r\n'
    response += str(data)
    new_socket.send(response.encode('gbk'))


def main():
    #创建套接字
    serve_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定ip和端口
    serve_socket.bind(('',5000))
    #listen客户端需求
    serve_socket.listen(128)
    #等待客户端链接accept
    new_socket,client_addr = serve_socket.accept()
    print(new_socket)
    print(client_addr)
    #服务客户端recv和send

        service_client(new_socket)


if __name__ == '__main__':

    main()