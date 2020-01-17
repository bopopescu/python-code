#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-06 15:35
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : kai.py
import socket,time
def wake_up(request, mac='DC-4A-3E-78-3E-0A'):
   MAC = mac
   BROADCAST = "10.168.5.136"
   if len(MAC) != 17:
       raise ValueError("MAC address should be set as form 'XX-XX-XX-XX-XX-XX'")
   mac_address = MAC.replace("-", '')
   data = ''.join(['FFFFFFFFFFFF', mac_address * 20])  # 构造原始数据格式
   send_data = b''

   # 把原始数据转换为16进制字节数组，
   for i in range(0, len(data), 2):
       send_data = b''
   print(send_data)

   # 通过socket广播出去，为避免失败，间隔广播三次
   try:
       sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
       sock.sendto(send_data, (BROADCAST, 7))
       time.sleep(1)
       sock.sendto(send_data, (BROADCAST, 7))
       time.sleep(1)
       sock.sendto(send_data, (BROADCAST, 7))
       return 1
       print("Done")
   except Exception as e:
       return HttpResponse()
       print(e)