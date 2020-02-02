# -*- coding:utf-8 -*-
import unittest
import init_env
from common.HttpUtils import HttpUtils
from common.base_test import run_tests
from common.cc import ResourcePark


class TestResourcePark(unittest.TestCase):
    def setUp(self):
        """
        测试用例初始化操作
        """
        self.r = HttpUtils()

    def tearDown(self):
        assert self.result.status_code == 200
        self.r.logJson(jsonStr=self.result.text)

    def test_config_json(self):
        """
        """
        data = {
            'companyId': '61e04cca-9213-451b-94ae-8d4dc2a1a5ea',
            'json': '{"resourceKey":"","resourceSecret":"","resourceEffectiveDuration":"","accountType":"1","userInfoFields":"name,fullName,email,phoneNumber,sex"}'
        }
        self.result = self.r.post(ResourcePark.CONFIG_JSON, data=data)


if __name__ == "__main__":
    tests = [
        # TestcompanyConfig('test_callbackConfig_insert'),
        # TestcompanyConfig('test_callbackConfig_update'),
        TestResourcePark('test_config_json'),
    ]
    run_tests(tests)
