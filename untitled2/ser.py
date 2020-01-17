import socket
import random
from yuyin import play
# 创建实例
sk = socket.socket()
# 定义IP和端口
ip_port = ("", 8000)
# 绑定监听
sk.bind(ip_port)
# 设置最大链接数
sk.listen(5)
# 轮询，不断的接收数据
while True:
    # 提示信息
    print("正在等待接收数据。。。。。")
    # 接收数据
    conn, address = sk.accept()
    # 定义信息
    msg = "链接成功!"
    # 返回信息 py3.x以上，网络数据的发送接收都是byte类型
    # str则需要编码
    conn.send(msg.encode())
    # 不断接收客户端发送的信息

    # 每次读取缓冲区1024字节的数据
    while 1:
        data = conn.recv(1024)
        # 打印数据,处理数据逻辑
        print(data)
        if data:
            conn.send(data)
        pass
