# -*- coding:utf-8 -*-
from init_env import BASE_DIR
from common.HttpUtils import HttpUtils
from common.cc import company_resource,get_token
from common.base_test import runTests
from unittest import TestCase

r = HttpUtils()


class TestCompanyResource(TestCase):
    """接入企业管理
    """

    def setUp(self):
        self.header = {'Authorization': get_token()}

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
            'providerIds': '019aa10e-6f14-4d87-9590-fd24a31821ac',
            'companyId': '000ed610-1e6f-4414-9783-e2810a2cb22e',
            'grantType': 1,
            'effectiveTime': '2019-08-04 12:00:00',
            'failureTime': '2019-09-05 12:00:00',
            'number': 10
        }
        self.result = r.post(
            company_resource.GRANT_RESOURCE_PROVIDER, data=data, headers=self.header)


if __name__ == "__main__":
    runTests([
        # TestCompanyResource("test_grant_resource"),
        TestCompanyResource("test_list")
    ])
