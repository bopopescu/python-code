#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-26 15:54
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py
from vibora import Vibora, Request
from vibora.responses import JsonResponse

app = Vibora()
@app.route('/')
async def home(request: Request):
    return JsonResponse({'hello': 'world'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, workers=1, debug=False)