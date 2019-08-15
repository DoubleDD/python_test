# -*- coding:utf-8 -*-
from init_env import BASE_DIR
from common.HttpUtils import HttpUtils
from common.cc import company_resource
from common.base_test import runTests
from unittest import TestCase

r = HttpUtils()


class TestCompanyResource(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        result = self.result
        r.logJson(jsonStr=result.text)
        assert result.status_code == 200, "请求状态码应为 200"

    def test_list(self):
        """接入企业管理列表接口
        """
        url = company_resource.LIST+"?page=1&pageSize=10"
        self.result = r.get(url)

    def test_grant_resource(self):
        """资源配置接口——按资源方对接
        """
        data = {
            'providerIds': '',
            'companyId': '',
            'grantType': 1,
            'effectiveTime': '2019-08-04 12:00:00',
            'failureTime': '2019-09-05 12:00:00',
            'number': 10
        }
        self.result = r.post(
            company_resource.GRANT_RESOURCE_PROVIDER, data=data)


if __name__ == "__main__":
    runTests([
        TestCompanyResource("test_grant_resource"),
        TestCompanyResource("test_list")
    ])
