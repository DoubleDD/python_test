#!/usr/bin/python
# -*- coding:utf-8 -*-
import init_env
from common.md5Utils import md5_sign

def originParam(str):
    data = {}
    params = str.split('&')
    for kv in params:
        if kv:
            arr = kv.split('=')
            if len(arr) == 2:
                k = kv.split('=')[0]
                v = kv.split('=')[1]
                data[k] = v
    return data


def buildParams(data,secret=None):
    sign = md5_sign(data, secret)
    data['sign'] = sign
    dataList = []
    for key in data:
        dataList.append("%s=%s" % (key, data[key]))
    params = '&'.join(dataList).strip()
    return params

def buildPostData(data,secret=None):
    sign = md5_sign(data, secret)
    data['sign'] = sign
    return data
