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
    debugParams = 'finishStatus=1&finishTime=0&apikey=a5c11b18ede548148f24&accountName=admin&organizationCode=zz_BAde1af01&sign=F9B8DF305E3A9E6BF90FC559070F3583&beginTime=1573609703984&courseId=27fcd65a-1dc8-421b-bf06-627ad86a6cdd&studyTotalTime=5&timestamp=1573609703984&'
# https://rasdev9.zhixueyun.com/api/v1/content/resource/learning/progress/subject?finishStatus=1&finishTime=0&apikey=a5c11b18ede548148f24&accountName=admin&organizationCode=zz_BAde1af01&sign=F9B8DF305E3A9E6BF90FC559070F3583&beginTime=1573609703984&courseId=27fcd65a-1dc8-421b-bf06-627ad86a6cdd&studyTotalTime=5&timestamp=1573609703984&
    test(debugParams)

