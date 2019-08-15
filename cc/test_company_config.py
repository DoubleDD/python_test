# -*- coding:utf-8 -*-
from init_env import BASE_DIR
from common.HttpUtils import HttpUtils
from common.cc import company_config
from common.base_test import runTests
import unittest


class TestcompanyConfig(unittest.TestCase):
    def setUp(self):
        '''
        测试用例初始化操作
        '''
        self.r = HttpUtils()

    def tearDown(self):
        assert self.result.status_code == 200
        self.r.logJson(jsonStr=self.result.text)

    def test_callbackConfig_insert(self):
        """新增企业鉴权接口配置信息
        """
        data = {
            'companyId': '61e04cca-9213-451b-94ae-8d4dc2a1a5ea',
            'callbackUrl': 'https://test9.zhixueyun.com/#/home'
        }
        self.result = self.r.post(company_config.CALLBACK_CONFIG, data=data)

    def test_callbackConfig_update(self):
        """修改企业鉴权接口配置信息
        """
        data = {
            'companyId': '61e04cca-9213-451b-94ae-8d4dc2a1a5ea',
            'callbackUrl': 'http://confluence.zhixueyun.com/pages/viewpage.action?pageId=14109785'
        }
        self.result = self.r.post(company_config.CALLBACK_CONFIG, data=data)


if __name__ == "__main__":
    tests = [
        TestcompanyConfig('test_callbackConfig_insert'),
        TestcompanyConfig('test_callbackConfig_update'),
    ]
    runTests(tests)
