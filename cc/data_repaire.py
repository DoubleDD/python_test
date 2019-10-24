#!/usr/bin/python
# -*- coding:utf-8 -*-
import init_env
from common.HttpUtils import HttpUtils

'''
统计数据修复程序
'''

rasdev9 = "rasdev9.zhixueyun.com"
rastest9 = "rastest9.zhixueyun.com"


domain = rasdev9

# 接入企业code
code='cmcc'
# 订单编号
orderNo='123'

companyUrl = f'https://{domain}/api/v1/content/test/statistic/update/1/{code}/{orderNo}'
orderUrl = f'https://{domain}/api/v1/content/test/statistic/update/2/{code}/{orderNo}'


def repaire(url):
    r = HttpUtils()
    result = r.get(url=url)
    r.logJson(jsonStr=result.text)


# 接入企业维度
repaire(companyUrl)

# 订单维度
# repaire(orderUrl)
