from socket import *
import json
def ser():
    s =socket(AF_INET, SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))

    s.listen(1)
    return s

# 自动判断url路径
def urlr(recvData):
    hh = list(str(recvData))
    print(hh)
    for i in range(len(hh)):
        if hh[i] == "H":
            su = i
            print(i)
            break
    filenam = str(recvData)
    print(su)
    filename = filenam[7:int(su-1)]
    print(filename)
    if filename:
        return filename
    else:
        return "index"


def cer():

    while 1:
        print("服务开启")
        c, clientInfo = ser().accept()
        # print(c.recv(1024),"\n",clientInfo)

        rt =str(urlr(c.recv(1024)))
        print(rt)
        c.send(b"HTTP/1.1 200 OK \r\n\r\n")
        try:
            if rt=="api":
                c.send("{'data':1}")
                # f = open(rt + ".html","rb")
                #
                # for value in f:
                #     if value:
                #         c.send(value)

            else:
                break

        except Exception as e:
            f = open("index.html", "rb")
            for aluer in f:

                c.send(aluer)

            print("传输异常：", e)



if __name__ =="__main__":
    cer()