import pymysql
def mysql():
    sqlr = pymysql.connect(host='127.0.0.1', user='root', password='root', database='820012', charset='utf8')
    print('mysql  ok')
    return sqlr.cursor()

def data1(vaule):
    r1 = mysql()
    r1.execute(vaule)
    return r1.fetchall()