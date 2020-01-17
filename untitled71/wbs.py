#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-12 10:45
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : wbs.py
#
# def el(yy):
#     from email.header import Header
#     from email.mime.text import MIMEText
#     from email.utils import parseaddr, formataddr
#     def _format_addr(s):
#         name, addr = parseaddr(s)
#         return formataddr((Header(name, 'utf-8').encode(), addr))
#
#     from_addr = "wapjin@qq.com"
#     password = "sczzaixuiuxobfhj"
#     to_addr = "1045833538@qq.com"
#     # print(str(html))
#     msg = MIMEText(str(yy), 'html', 'utf-8')
#     msg['From'] = _format_addr('admin <%s>' % from_addr)
#     msg['To'] = _format_addr('you <%s>' % to_addr)
#     msg['Subject'] = Header('xinhaiadmin', 'utf-8').encode()
#     import smtplib
#     server = smtplib.SMTP_SSL("smtp.qq.com", 465)
#     server.set_debuglevel(1)
#     server.login(from_addr, password)
#     server.sendmail(from_addr, [to_addr], msg.as_string())
#     server.quit()
#
# import urllib.request
# import re,time
# timer=str(str(time.strftime("%Y.%m.%d %H.%M.%S", time.localtime())))
# x = "慈溪天气"
# x = urllib.parse.quote(x)
# link = urllib.request.urlopen(
#     "http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22" + x + "%22%7D%2C%22type%22%3A%22txt%22%7D")
# html_doc = link.read().decode()
# reply_list = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)
# el("早上好,我是小i：时间"+timer +","+ reply_list[-1])
import urllib.request
import re,time
def el(yy):
    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = "wapjin@qq.com"
    password = "sczzaixuiuxobfhj"
    to_addr = "1045833538@qq.com"
    # print(str(html))
    msg = MIMEText(str(yy), 'html', 'utf-8')
    msg['From'] = _format_addr('天气 <%s>' % from_addr)
    msg['To'] = _format_addr('you <%s>' % to_addr)
    msg['Subject'] = Header('天气提醒', 'utf-8').encode()
    import smtplib
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


timer=str(str(time.strftime("%Y.%m.%d %H.%M.%S", time.localtime())))
x = "慈溪天气"
x = urllib.parse.quote(x)
link = urllib.request.urlopen(
  "http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22" + x + "%22%7D%2C%22type%22%3A%22txt%22%7D")
html_doc = link.read().decode()
reply_list = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)
el("早上好,我是小i：时间"+timer +","+ reply_list[-1])





