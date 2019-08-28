# -*- coding:utf-8 -*-
import init_env
from common.HttpUtils import HttpUtils
from common.cc import CompanyResource, get_token
from common.base_test import run_tests
from unittest import TestCase

r = HttpUtils()


class TestCompanyResource(TestCase):
    """接入企业管理
    """

    def setUp(self):
        self.header = {'Authorization': get_token()}

    def tearDown(self):
        result = self.result
        print("\n接口响应：")
        r.logJson(jsonStr=result.text)
        assert result.status_code == 200, "请求状态码应为 200"

    def test_list(self):
        """接入企业管理列表接口
        """
        page = 1
        page_size = 20
        uri = 'human/access-enterprise'
        company_name = '米'
        params = f'?page={page}&pageSize={page_size}&uri={uri}&companyName={company_name}'
        url = CompanyResource.LIST + params
        self.result = r.get(url, headers=self.header)

    def test_grant_resource(self):
        """资源配置接口——按资源方对接
        """
        data = {
            'providerIds': 'b7c4911b-2064-434b-aa26-2c4a86f183af',
            'companyId': '64d63434-b903-425f-ab39-bcb1e2332fb5',
            'grantType': 1,
            'effectiveTime': '2019-08-15 00:00',
            'failureTime': '2019-09-05 12:00',
            'number': 10
        }
        self.result = r.post(
            CompanyResource.GRANT_RESOURCE_PROVIDER, data=data, headers=self.header)


if __name__ == "__main__":
    run_tests([
        # TestCompanyResource("test_grant_resource"),
        TestCompanyResource("test_list")
    ])
