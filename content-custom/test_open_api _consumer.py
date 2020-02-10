#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import init_env
from unittest import TestCase
from common.base_test import run_tests
from common.cc import ConsumerLearningProgress
from common.HttpUtils import HttpUtils
from common.md5Utils import md5_sign
from common.paramTools import originParam, buildParams
from common.DateUtils import currentTimeMillis


r = HttpUtils()
'''
资源平台admin账号信息
'''
user_info = {
    "organizationCode": "cmcc",  # dev
    # "organizationCode": "zz_BA503b5123",#test
    "accountName": "admin"
}

isDebug = 1


class TestConsumerLearningProgress(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        result = self.result
        print("\n接口响应：")
        r.logJson(jsonStr=result.text)
        assert result.status_code == 200, "请求状态码应为 200"

    def test_course(self):
        """
        课程数据回传接口
        """
        # mock 参数
        data = {
            'apikey': ConsumerLearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'name': user_info['accountName'],
            'organizationCode': user_info['organizationCode'],
            "courseId": "db15a39f-5c82-433a-ba83-a42123422f85",
            "finishStatus": "0",
            "studyTotalTime": "0",
        }

        if isDebug:
            # 联调参数
            debugParams = 'finishStatus=0&apikey=e61121d3d39f649c1f847e470abf2e95&name=admin&organizationCode=cmcc&sign=B80DE72362206CFE54C73F9BA9A05155&courseId=db15a39f-5c82-433a-ba83-a42123422f85&studyTotalTime=0&timestamp=1580649104872'
            # 处理原始参数
            data = originParam(debugParams)

        print(r.toJsonString(data))

        url = 'http://localhost:8086/api/v1/course-study/resource/learning/progress/course'
        self.result = r.post(url=url, data=buildParams(data,ConsumerLearningProgress.SECRET_KEY))

    def test_activity(self):
        """
        外部活动数据回传接口
        """
        # mock 参数
        data = {
            'apikey': ConsumerLearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'name': user_info['accountName'],
            'organizationCode': user_info['organizationCode'],
            'externalActivityId': 'd595bda0-0e83-42ce-837e-4e0629f69b95',
            'studyStatus': 2
        }

        if isDebug:
            # 联调参数
            debugParams = 'apikey=e61121d3d39f649c1f847e470abf2e95&name=admin&organizationCode=cmcc&externalActivityId=541f4c59-690a-4aec-8eb3-253f175c70ba&sign=1DA098D37909C254266A6977F6FB5E6C&timestamp=1580651804318&studyStatus=1'
            # 处理原始参数
            data = originParam(debugParams)

        url = 'http://localhost:8086/api/v1/course-study/resource/learning/progress/externalActivity'
        self.result = r.post(url=url, data=buildParams(data,ConsumerLearningProgress.SECRET_KEY))

    def test_subject(self):
        """
        学习专题数据回传接口
        """
        # mock 参数
        data = {
            'apikey': ConsumerLearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'name': user_info['accountName'],
            'organizationCode': user_info['organizationCode'],
            'courseId': 'c5526fe0-edc6-4bd6-8c25-1e840b82ab80',
            'finishStatus': 1,
            'finishTime': '',
            'beginTime': int(currentTimeMillis()*1000),
            'finishNum': 0,
            'studyTotalTime': 1111111
        }

        if isDebug:
            # 联调参数
            debugParams = 'finishStatus=1&finishTime=&apikey=e61121d3d39f649c1f847e470abf2e95&name=admin&organizationCode=cmcc&sign=A87096F9C698CB141F2AC81B7FD3B3D0&beginTime=1580631436742&courseId=acc681d3-3c74-44bc-80f4-86dfefb10dbf&finishNum=0&studyTotalTime=1111111&timestamp=1580649261100'

            # 处理原始参数
            data = originParam(debugParams)

        url = 'http://localhost:8086/api/v1/course-study/resource/learning/progress/subject'
        self.result = r.post(url=url, data=buildParams(data,ConsumerLearningProgress.SECRET_KEY))


if __name__ == '__main__':
    run_tests([
        # TestConsumerLearningProgress('test_course'),
        TestConsumerLearningProgress('test_subject'),
        # TestConsumerLearningProgress('test_activity'),
    ])
