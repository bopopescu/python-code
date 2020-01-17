#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-21 10:28
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : wence.py
import socket

# 创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
# 连接IP地址和端口

tcp_client_socket.connect(("127.0.0.1", 8080))

file_name = input("请输入要下载的文件：\n")
# 文件名编码
tcp_client_socket.send(file_name.encode())
try:
    # 文件传输
    with open(file_name, "wb") as file:
        while True:
            # 接收数据
            file_data = tcp_client_socket.recv(1024)
            # 数据长度不为0写入文件
            if file_data:
                # print(len(file_data))
                file.write(file_data)
            # 数据长度为0表示下载完成
            else:
                break
# 下载出现异常时捕获异常
except Exception as e:
    print("下载异常", e)
# 无异常则下载成功
else:
    print(file_name, "下载成功")
    file.close()
tcp_client_socket.close()
# 关闭客户端

