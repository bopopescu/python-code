#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-12 10:09
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : reads.py

import random
def randoms():
    temp = [i + 1 for i in range(35)]
    random.shuffle(temp)

    i = 0

    list = []
    while i <= 0:
        list.append(temp[i])
        i = i + 1
    list.sort()
    print('\033[0;31;;1m')

    return list[-1]

print(randoms())