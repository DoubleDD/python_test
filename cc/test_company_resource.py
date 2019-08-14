# -*- coding:utf-8 -*-
from init_env import BASE_DIR
from common.HttpUtils import HttpUtils
from common.cc import company_resource
from common.base_test import runTests
import unittest


class TestCompanyResource(unittest.TestCase):
    def setUp(self):
        """前置设置
        """
        self.r = HttpUtils()

    def tearDown(self):
        pass

    def test_list(self):
        """接入企业管理列表接口
        """
        url = company_resource.list+"?page=1&pageSize=10"
        result = self.r.get(url)
        self.r.logJson(jsonStr=result.text)
        assert result.status_code == 200, "失败"


if __name__ == "__main__":
    runTests([
        TestCompanyResource("test_list")
    ])
