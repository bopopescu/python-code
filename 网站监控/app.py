from req import getreq
from sql import data1
import time
import smtplib
from email.mime.text import MIMEText
import json

errurl = []
def main(url1):
    txt = getreq(url1)
    times = str(str(time.strftime("%Y.%m.%d %H.%M.%S", time.localtime())))

    if txt!= 1:
        print(txt[:3])
        codes = data1("INSERT INTO datas (url,time,code) VALUES ('"+url1+"','"+times+"','"+txt[:3]+"')")

        errurl.append(url1)

        # send_email("服务器出现问题！  点击链接查看详细：http://wapjin.com")
        # print("fasong")
        print("err:" + url1)


    else:
        print("服务正常"+url1)







def send_email(content):
    sender = "wapjin@qq.com"
    password="ypqknprfwsoibfbd"
    receiver = ["wapjin@qq.com"]
    host = 'smtp.qq.com'
    port = 465
    msg = MIMEText(content)
    msg['From'] = "wapjin@qq.com"
    msg['To'] = "wapjin@qq.com"
    msg['Subject'] = "system error warning"

    try:
        smtp = smtplib.SMTP_SSL(host, port)
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, msg.as_string())

    except Exception as e:

        pass


if __name__ == "__main__":
    while 1:
        with open("url.json", 'r') as load_f:

            load_dict = json.load(load_f)
        crr = load_dict["data"]
        for i in range(len(crr)):

            if len(errurl)==0:
                main(crr[i])
            # print(errurl)
            for t in errurl:
                # print(t)
                if t!=crr[i]:

                    main(crr[i])
                else:
                    crr.remove(t)
        if str(str(time.strftime("%H:%M", time.localtime())))=="12:00":
            for i in errurl:
                crr.append(t)
        else:
            time.sleep(2*60)





    # main("http://wapjin.com/pp.html")