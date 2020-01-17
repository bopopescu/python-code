#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-14 15:10
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : aps.py

global result, err
import time
import requests
import os
import signal

# Prompt email sending
cmd = 'java -jar /home/tomcat/jar/tcp-server.jar'
url = 'http://192.168.0.100:8080/flow/connec'
# to_addr = "hudongdong@xinhaigroup.com"
to_addr = "1045833538@qq.com"
port = 8080


def kill_process(port):
    pid = \
    os.popen("netstat -nlp | grep :%s | awk '{print $7}' | awk -F\" / \" '{ print $1 }'" % (port)).read().split('/')[0]
    a = os.system("kill -9 " + pid)
    print(1)
    print(a)
    time.sleep(2)
    # print()
    # if os.kill(pid, signal.SIGKILL):
    #     print('ok')
    #     time.sleep(20)
    #     return 1
    # else:
    return a


def GetEl(vaule):
    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = "wapjin@qq.com"
    password = "sczzaixuiuxobfhj"
    # print(str(html))
    msg = MIMEText(str(vaule), 'html', 'utf-8')
    msg['From'] = _format_addr(' Constant flow valve service <%s>' % from_addr)
    msg['To'] = _format_addr('you <%s>' % to_addr)
    msg['Subject'] = Header('Program warning', 'utf-8').encode()
    import smtplib
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


# Constant flow valve service access
def Gethtml():
    headers = {"User_Agent": "Mozilla/5.0(compatible; MSIE 5.5; Windows 10)"}
    try:
        r = requests.get(url, headers=headers)
        return str(r.text)
    except IOError as e:
        return str(3)


# ssh start
def ssh_connect():
    return os.system(cmd)


# main program
def apps():
    i = 1
    while 1:

        print("start")
        tr = Gethtml()
        if int(len(tr)) > 2:

            if int(kill_process(port)) == 0:
                result = ssh_connect()
                print(result)
                if result > 0:
                    timedata = str(str(time.strftime("%Y.%m.%d %H.%M.%S", time.localtime())))

                    err = "errtime:" + timedata + "\n"
                    f = open('log.txt', 'a+')
                    f.write(err)
                    f.close()
                    while result:
                        time.sleep(5)
                        print(i)
                        kill_process(port)
                        result = ssh_connect()
                        i = i + 1
                        if i > 4:
                            break
                        if result == 0:
                            break

            else:
                timedata = str(str(time.strftime("%Y.%m.%d %H.%M.%S", time.localtime())))
                print("err")
                err = "errtime:" + timedata + "\n"
                f = open('log.txt', 'a+')
                f.write(err)
                f.close()
                i = i + 1
        print(i)
        if i > 4:
            GetEl(err)
            break

        if i > 6:
            break
        time.sleep(30)


while 1:
    apps()