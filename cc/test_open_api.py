#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import init_env
from unittest import TestCase
from common.base_test import run_tests
from common.cc import LearningProgress, UserInfo
from common.HttpUtils import HttpUtils
from common.md5Utils import md5_sign
from common.DateUtils import currentTimeMillis


r = HttpUtils()
'''
资源平台admin账号信息
1572505157.3871675
'''
user_info = {
    "msg": "success",
    "phoneNumber": None,
    "rootOrganizationCode": "zz_BAde1af01",
    "headPortraitPath": None,
    "sex": 0,
    "name": "admin",
    "rootOrganizationName": "资源共享平台",
    "fullName": "超级管理员",
    "id": "45626218-a4fc-41eb-8c66-022886421a10",
    "headPortrait": None,
    "rootOrganizationId": "ba915d93-274d-4319-8016-035508166f64",
    "email": None
}


class TestLearningProgress(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        result = self.result
        print("\n接口响应：")
        r.logJson(jsonStr=result.text)
        assert result.status_code == 200, "请求状态码应为 200"

    def buildParams(self, data):
        sign = md5_sign(data, LearningProgress.SECRET_KEY)
        data['sign'] = sign
        dataList = []
        for key in data:
            dataList.append("%s=%s" % (key, data[key]))
        params = '&'.join(dataList).strip()
        return params

    def test_course(self):
        """
        课程数据回传接口
        @Param(name = "name", required = true)
        @Param(name = "organizationCode", required = true)
        @Param(name = "courseId", required = true)
        @Param(name = "sign", required = true)
        @Param(name = "finishStatus", type = Integer.class, required = true)
        @Param(name = "finishTime", type = Long.class)
        @Param(name = "studyTotalTime", type = Integer.class, required = true)
        """
        data = {
            'apikey': LearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'accountName': user_info['name'],
            'organizationCode': user_info['rootOrganizationCode'],
            'courseId': '3c724f7e-7153-4090-abe9-bb8d1d5a4b70',
            'finishStatus': 1,
            # 'finishTime': int(currentTimeMillis()*1000),
            'studyTotalTime': 1111111
        }
        url = LearningProgress.course+'?'+self.buildParams(data)
        self.result = r.get(url)

    def test_activity(self):
        """
        外部活动数据回传接口
        @Param(name = "sign", required = true)
        @Param(name = "apikey", required = true)
        @Param(name = "timestamp", required = true)
        @Param(name = "accountName", required = true)
        @Param(name = "organizationCode", required = true)
        @Param(name = "externalActivityId", required = true)
        @Param(name = "seconds", type = Integer.class)
        @Param(name = "obligatoryFinished", type = Integer.class)
        @Param(name = "obligatoryTotal", type = Integer.class)
        @Param(name = "obligatoryUnit", type = Integer.class)
        @Param(name = "electiveFinished", type = Integer.class)
        @Param(name = "electiveTotal", type = Integer.class)
        @Param(name = "electiveUnit", type = Integer.class)
        @Param(name = "examStatus", type = Integer.class)
        @Param(name = "taskStatus", type = Integer.class)
        @Param(name = "studyStatus", type = Integer.class, required = true)
        @Param(name = "finishTime", type = Long.class)
        """
        data = {
            'apikey': LearningProgress.API_KEY+'1',
            'timestamp': int(currentTimeMillis()*1000),
            'accountName': user_info['name'],
            'organizationCode': user_info['rootOrganizationCode'],
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

        url = LearningProgress.external_activity+'?'+self.buildParams(data)
        self.result = r.get(url)

    def test_subject(self):
        """
        学习专题数据回传接口
        @Param(name = "sign", required = true)
        @Param(name = "apikey", required = true)
        @Param(name = "timestamp", required = true)
        @Param(name = "accountName", required = true)
        @Param(name = "organizationCode", required = true)
        @Param(name = "courseId", required = true)
        @Param(name = "finishStatus", type = Integer.class, required = true)
        @Param(name = "beginTime", type = Long.class)
        @Param(name = "finishTime", type = Long.class)
        @Param(name = "studyTotalTime", type = Integer.class, required = true)
        @Param(name = "finishNum", type = Integer.class)
        """
        data = {
            'apikey': LearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'accountName': user_info['name'],
            'organizationCode': user_info['rootOrganizationCode'],
            'courseId': '3c724f7e-7153-4090-abe9-bb8d1d5a4b70',
            'finishStatus': 1,
            'finishTime': int(currentTimeMillis()*1000),
            'beginTime': int(currentTimeMillis()*1000),
            'finishNum': 0,
            'studyTotalTime': 1111111
        }

        url = LearningProgress.subject+'?'+self.buildParams(data)
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
        url = UserInfo.url+'?'+self.buildParams(data)
        self.result = r.get(url)


if __name__ == '__main__':
    run_tests([
        # TestLearningProgress('test_course'),
        # TestLearningProgress('test_subject'),
        # TestLearningProgress('test_activity'),
        TestLearningProgress('test_userInfo'),
    ])
