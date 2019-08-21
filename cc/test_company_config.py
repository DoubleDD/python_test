# -*- coding:utf-8 -*-
import unittest
import init_env
from common.HttpUtils import HttpUtils
from common.base_test import run_tests
from common.cc import company_config


class TestcompanyConfig(unittest.TestCase):
    def setUp(self):
        """
        测试用例初始化操作
        """
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

    def test_callbackConfig_get(self):
        """查询企业鉴权接口配置信息
        """
        company_id = '61e04cca-9213-451b-94ae-8d4dc2a1a5ea'
        url = company_config.CALLBACK_CONFIG + f'?companyId={company_id}'
        self.result = self.r.get(url)


if __name__ == "__main__":
    tests = [
        # TestcompanyConfig('test_callbackConfig_insert'),
        # TestcompanyConfig('test_callbackConfig_update'),
        TestcompanyConfig('test_callbackConfig_get'),
    ]
    run_tests(tests)
