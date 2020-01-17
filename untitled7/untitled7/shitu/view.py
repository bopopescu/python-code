#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-04 10:19
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : view.py
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from ..mysql import *
def book(request):

    row = data("select * from jin ")
    arr=[]
    for i in row:
        arr.append(i)
    test={
        'msg':1,
        'data':arr

    }
    return HttpResponse(getjson(test))

def bookurl(request):
    id= request.GET.get('id')
    test="id为：%s" % id
    return JsonResponse(test,safe=False)
def index(request):
    return render(request,'index.html')