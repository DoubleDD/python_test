"""open api test
"""
# -*- coding:utf-8 -*-
#!/usr/bin/python
from unittest import TestCase
from common.base_test import run_tests
from common.cc import LearningProgress, UserInfo
from common.HttpUtils import HttpUtils
from common.md5Utils import md5_sign
from common.paramTools import originParam, buildParams, buildPostData
from common.DateUtils import currentTimeMillis

import init_env

r = HttpUtils()
'''
资源平台admin账号信息
'''
user_info = {
    "organizationCode": "zz_BAde1af01",  # dev
    # "organizationCode": "zz_BA503b5123",#test
    "accountName": "cmccadmin"
}

isDebug = 0


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
        data = {"finishStatus": 2, "finishTime": 1583640517384, "apikey": "97dab5d238c75a1d3dad89faa9df03e4", "accountName": "hgydx13547198687wxj#", "organizationCode": "zz_BA43ef5ab5", "sign": "B545D08FCE451B0BD4D388D6672ED8EA",
                "beginTime": 1583638573887, "courseId": "26DB841A84140C58A8A9A5DAA8A4A1FB03B75F3A13594D8832E7A1240183096B099D10AA1B1BB22C", "studyTotalTime": 1665, "timestamp": "1583640877461"}

        if isDebug:
            # 联调参数
            debugParams = 'finishStatus=0&finishTime=0&apikey=a5c11b18ede548148f24&accountName=%E8%AF%BE%E7%A8%8B%E6%B5%8B%E8%AF%952019103001&organizationCode=%E8%AF%BE%E7%A8%8B%E6%B5%8B%E8%AF%952019103001&sign=85715FA4D8A792CCF9DF7E35294A03A3&courseId=1&studyTotalTime=5&timestamp=1573537557170& '
            # 处理原始参数
            data = originParam(debugParams)
        # serverUrl = LearningProgress.course;
        # serverUrl = 'https://rastest9.zhixueyun.com/api/v1/content/resource/learning/progress/course'
        serverUrl = 'http://localhost:8888/api/v1/content/resource/learning/progress/course'
        url = serverUrl + '?' + buildParams(data,'123')
        self.result = r.get(url)

    def test_activity(self):
        """
        外部活动数据回传接口
        """
        # mock 参数
        data = {
            'apikey': LearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'accountName': user_info['accountName'],
            'organizationCode': user_info['organizationCode'],
            'externalActivityId': 'd595bda0-0e83-42ce-837e-4e0629f69b95',
            'studyStatus': 2
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
        # mock 参数
        data = {
            'apikey': LearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'accountName': user_info['accountName'],
            'organizationCode': user_info['organizationCode'],
            'courseId': 'c5526fe0-edc6-4bd6-8c25-1e840b82ab80',
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
        # mock 参数
        data = {
            'apikey': LearningProgress.API_KEY,
            'timestamp': int(currentTimeMillis()*1000),
            'token': 'ea992d3ec553203e25032b5a5dd72510'
        }
        url = 'https://zxhcs.zhixueyun.com/api/v1/content/user/info/simple?' + \
            buildParams(data, LearningProgress.SECRET_KEY)
        # url = UserInfo.url+'?'+buildParams(data,LearningProgress.SECRET_KEY)
        #     API_KEY = '8bf8e66924e3f63453842084995354d6'
        # SECRET_KEY = 'd7247877a06de4b0ed2d9825d6ed134a'
        self.result = r.get(url)

    def test_course_batch(self):
        """
        课程数据回传接口
        """
        # mock 参数
        data = {
            "apikey": "3466ea0c6911ebec017c89e18c21892e",
            "timestamp": "1582544727196", "organizationCode": "zz_BAde1af01",
            "progress": "[{\"finishStatus\":\"1\",\"accountName\":\"cmccadmin\",\"organizationCode\":\"zz_BAde1af01\",\"beginTime\":\"1580203838730\",\"courseId\":\"000ebb2e-69c8-497b-8ab1-c54138322e05\",\"studyTotalTime\":\"600\"},{\"finishStatus\":\"1\",\"accountName\":\"cmccadmin\",\"organizationCode\":\"zz_BAde1af01\",\"beginTime\":\"1580203838730\",\"courseId\":\"000ebb2e-69c8-497b-8ab1-c54138322e05\",\"studyTotalTime\":\"600\"},{\"finishStatus\":\"1\",\"accountName\":\"cmccadmin\",\"organizationCode\":\"zz_BAde1af01\",\"beginTime\":\"1580203838730\",\"courseId\":\"000ebb2e-69c8-497b-8ab1-c54138322e05\",\"studyTotalTime\":\"600\"}]"
        }

        if isDebug:
            # 联调参数
            debugParams = 'finishStatus=0&finishTime=0&apikey=a5c11b18ede548148f24&accountName=%E8%AF%BE%E7%A8%8B%E6%B5%8B%E8%AF%952019103001&organizationCode=%E8%AF%BE%E7%A8%8B%E6%B5%8B%E8%AF%952019103001&sign=85715FA4D8A792CCF9DF7E35294A03A3&courseId=1&studyTotalTime=5&timestamp=1573537557170& '
            # 处理原始参数
            data = originParam(debugParams)

        domain = 'http://localhost:8888'
        path = '/api/v1/content/resource/learning/progress/course/batch'

        data = buildPostData(data, '903a1b14ebbec7a24ce3ce762dca7008')

        self.result = r.post(url=domain+path, data=data)


if __name__ == '__main__':
    run_tests([
        # TestLearningProgress('test_userInfo'),
        # TestLearningProgress('test_course_batch'),
        TestLearningProgress('test_course'),
        # TestLearningProgress('test_subject'),
        # TestLearningProgress('test_activity'),
    ])
