#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import init_env
from unittest import TestCase
from common.base_test import run_tests
from common.cc import LearningProgress, UserInfo
from common.HttpUtils import HttpUtils
from common.md5Utils import md5_sign
from common.paramTools import originParam, buildParams
from common.DateUtils import currentTimeMillis


r = HttpUtils()
'''
资源平台admin账号信息
'''
user_info = {
    "organizationCode": "zz_BAde1af01",#dev
    # "organizationCode": "zz_BA503b5123",#test
    "accountName": "admin"
}

isDebug=0

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

        if isDebug:
            # 联调参数
            debugParams = 'finishStatus=0&finishTime=0&apikey=a5c11b18ede548148f24&accountName=%E8%AF%BE%E7%A8%8B%E6%B5%8B%E8%AF%952019103001&organizationCode=%E8%AF%BE%E7%A8%8B%E6%B5%8B%E8%AF%952019103001&sign=85715FA4D8A792CCF9DF7E35294A03A3&courseId=1&studyTotalTime=5&timestamp=1573537557170& '
            # 处理原始参数
            data = originParam(debugParams)

        url = LearningProgress.course+'?'+buildParams(data)
        self.result = r.get(url)

    def test_activity(self):
        """
        外部活动数据回传接口
        """
        data = {
            'apikey': LearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'accountName': user_info['accountName'],
            'organizationCode': user_info['organizationCode'],
            'externalActivityId': '89fea018-09fd-429e-ad0a-06d59bb4fab0',
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

        if isDebug:
            # 联调参数
            debugParams = 'electiveUnit=1&apikey=a5c11b18ede548148f24&obligatoryFinished=1&accountName=admin&obligatoryTotal=3&sign=D2DEF11F4B127E69270E63FA92D24E57&obligatoryUnit=1&seconds=10&organizationCode=zz_BAde1af01&externalActivityId=cee5bbff-05de-11ea-843a-00163e11d483&electiveTotal=1&electiveFinished=0&timestamp=1573627257470&studyStatus=1&'
            # 处理原始参数
            data = originParam(debugParams)

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

        if isDebug:
            # 联调参数
            debugParams = 'finishStatus=1&finishTime=0&apikey=a5c11b18ede548148f24&accountName=admin&organizationCode=zz_BAde1af01&sign=F9B8DF305E3A9E6BF90FC559070F3583&beginTime=1573609703984&courseId=27fcd65a-1dc8-421b-bf06-627ad86a6cdd&studyTotalTime=5&timestamp=1573609703984&'

            # 处理原始参数
            data = originParam(debugParams)

        url = LearningProgress.subject+'?'+buildParams(data)
        self.result = r.get(url)

    def test_userInfo(self):
        """
        获取用户信息
        """
        data = {
            'apikey': LearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'token': '9176562f0b2e98eb6051197a03b14bf8'
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
