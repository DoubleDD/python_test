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
    debugParams = 'finishStatus=1&finishTime=0&apikey=a5c11b18ede548148f24&accountName=admin&organizationCode=zz_BA503b5123&sign=6AD6095B55E980451DB3DC50A55009AA&courseId=85976dae-1528-4724-ac13-cb7d8fd96627&studyTotalTime=5&timestamp=1573543507376&'

    test(debugParams)

