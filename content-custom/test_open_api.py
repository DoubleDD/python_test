#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import init_env
from unittest import TestCase
from common.base_test import run_tests
from common.cc import LearningProgress, UserInfo
from common.HttpUtils import HttpUtils
from common.md5Utils import md5_sign
from common.paramTools import originParam,buildParams
from common.DateUtils import currentTimeMillis


r = HttpUtils()
'''
资源平台admin账号信息
1572505157.3871675
'''
user_info = {
    "organizationCode": "zz_BAde1af01",
    "accountName": "admin"
}


class TestLearningProgress(TestCase):
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
            'apikey': LearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'accountName': user_info['accountName'],
            'organizationCode': user_info['organizationCode'],
            'courseId': 'da4d3b54-011d-4f08-88f9-0989fac1a6e4',
            'finishStatus': 1,
            'finishTime': int(currentTimeMillis()*1000),
            'studyTotalTime': 1111
        }

        # 联调参数
        debugParams = 'finishStatus=0&finishTime=0&apikey=a5c11b18ede548148f24&accountName=%E8%AF%BE%E7%A8%8B%E6%B5%8B%E8%AF%952019103001&organizationCode=%E8%AF%BE%E7%A8%8B%E6%B5%8B%E8%AF%952019103001&sign=85715FA4D8A792CCF9DF7E35294A03A3&courseId=1&studyTotalTime=5&timestamp=1573537557170& '

        # 处理原始参数
        # data = originParam(debugParams)

        url = LearningProgress.course+'?'+buildParams(data)
        self.result = r.get(url)

    def test_activity(self):
        """
        外部活动数据回传接口
        """
        data = {
            'apikey': LearningProgress.API_KEY+'1',
            'timestamp': int(currentTimeMillis()*1000),
            'accountName': user_info['accountName'],
            'organizationCode': user_info['organizationCode'],
            'externalActivityId': '3c724f7e-7153-4090-abe9-bb8d1d5a4b70',
            'seconds': 1,
            'obligatoryFinished': 0,
            'obligatoryTotal': 0,
            'obligatoryUnit': 0,
            'electiveFinished': 0,
            'electiveTotal': 0,
            'electiveUnit': 0,
            'examStatus': 0,
            'taskStatus': 0,
            'studyStatus': 0,
            'finishTime': int(currentTimeMillis()*1000),
        }

        url = LearningProgress.external_activity+'?'+buildParams(data)
        self.result = r.get(url)

    def test_subject(self):
        """
        学习专题数据回传接口
        """
        data = {
            'apikey': LearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'accountName': user_info['accountName'],
            'organizationCode': user_info['organizationCode'],
            'courseId': '3c724f7e-7153-4090-abe9-bb8d1d5a4b70',
            'finishStatus': 1,
            'finishTime': int(currentTimeMillis()*1000),
            'beginTime': int(currentTimeMillis()*1000),
            'finishNum': 0,
            'studyTotalTime': 1111111
        }

        url = LearningProgress.subject+'?'+buildParams(data)
        self.result = r.get(url)

    def test_userInfo(self):
        """
        获取用户信息
        """
        data = {
            'apikey': LearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'token': 'e9535fcefaac0344125f24d16f5805c8'
        }
        url = UserInfo.url+'?'+buildParams(data)
        self.result = r.get(url)




if __name__ == '__main__':
    run_tests([
        TestLearningProgress('test_course'),
        # TestLearningProgress('test_subject'),
        # TestLearningProgress('test_activity'),
        # TestLearningProgress('test_userInfo'),
    ])
