#!/usr/bin/python
# -*- coding:utf-8 -*-
import hashlib


def data_processing(data):
    """
    :param data: 需要签名的数据，字典类型
    :return: 处理后的字符串，格式为：参数名称=参数值，并用&连接
    """
    origin=[]
    for key in data:
        origin.append('%s=%s' % (key, data[key]))
    print("\n原始参数\n"+"&".join(origin).strip())

    if "sign" in data:
        del data["sign"]
    if "sign_type" in data:
        del data["sign_type"]
    dataList = []
    paramList = []
    for key in sorted(data):
        paramList.append('%s=%s' % (key, data[key]))
        dataList.append("%s%s" % (key, data[key]))
    # 排序后的参数
    result = "&".join(paramList).strip()
    print('\n排序后的参数\n'+result)
    # 拼接后的字符串
    result = "".join(dataList).strip()
    print('\n拼接后的字符串\n'+result)
    return result


def md5_sign(data, secret_key):
    """
    MD5签名
    :param secret_key: MD5签名需要的字符串
    :return: 签名后的字符串sign
    """
    data = secret_key.strip()+data_processing(data)+secret_key.strip()
    print('\n头尾添加secret\n'+data)
    return buildSign(data)


def buildSign(data):
    md5 = hashlib.md5()
    md5.update(data.encode(encoding='UTF-8'))
    byteArr = md5.digest()
    sign = byteArr.hex().upper()
    print('\nclient sign：\n'+sign)
    return sign


if __name__ == '__main__':
    ss = 'abc'
    buildSign(ss)
