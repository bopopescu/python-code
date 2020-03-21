import requests
def getreq(url):
    urlarr =[]
    g=''
    for i in range(5):
        urlarr.append(requests.get(url).status_code)
    for t in urlarr:
            g +=str(t)


    if str(g)[:3] =="200":
        return 1
    else:
        return g


