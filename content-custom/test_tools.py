#!/usr/bin/python
# -*- coding:utf-8 -*-
import init_env
from common.paramTools import originParam,buildParams

def test(debugParams):
    print('\n-------------------------------------\n')
    # 处理原始参数
    data = originParam(debugParams)
    originSign = data['sign']
    result = buildParams(data)
    print('原始签名：\n'+originSign)
    print('\nok\n-------------------------------------\n')
    return result

if __name__ == "__main__":
    # 联调参数
    debugParams = 'finishStatus=0&finishTime=0&apikey=a5c11b18ede548148f24&accountName=%E8%AF%BE%E7%A8%8B%E6%B5%8B%E8%AF%952019103001&organizationCode=%E8%AF%BE%E7%A8%8B%E6%B5%8B%E8%AF%952019103001&sign=85715FA4D8A792CCF9DF7E35294A03A3&courseId=1&studyTotalTime=5&timestamp=1573537557170& '

    test(debugParams)

