#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-17 15:48
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : imgrt.py
import requests
import json
def Getr():
    baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    #API Key
    client_id = "qTDpXcUl27LempcNVnP6GpKI"
    #Secret Key
    client_secret = "KMBW0bae3OcLeNCIzdOMdQINBEaNsiz3"

    #拼url
    url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(client_id, client_secret)
    #print(url)
    res = requests.post(url)
    #print(res.text)
    token = json.loads(res.text)["access_token"]
    return token
import urllib.parse, urllib.request, base64
def imgtext(urlk):
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + Getr()

    f = open(r"" + urlk, 'rb')

    img = base64.b64encode(f.read())
    params = {"image": img}
    params = urllib.parse.urlencode(params).encode(encoding='UTF8')
    request = urllib.request.Request(url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()

    return content
def imgma(val):
    return str(json.loads(imgtext(val))['words_result'][0]['words'])
