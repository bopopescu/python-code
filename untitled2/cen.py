import socket
from yuyin import LuYin
# 实例初始化
client = socket.socket()
# 访问的服务器端口和ip
ip_port = ("127.0.0.1", 8000)
# 链接服务器
client.connect(ip_port)

while True:
    # 接收主机信息
    data = client.recv(1024)
    # 打印接收的数据,此处的byte数据特指py3.x以上
    print(data)
    # 消息发送
    print(LuYin())
    client.send(LuYin())
    data = client.recv(1024)
    if data:
        print('接收')
        # 打印接收的数据,此处的byte数据特指py3.x以上
        from yuyin import play
        play(data)
        print(data)
pass
