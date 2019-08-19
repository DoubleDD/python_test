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
        print("\n接口响应：")
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
            'providerIds': '3166ddf9-bbfd-4f24-b686-4a4ee887cabb,c670ee7f-a0b5-4c9d-ae7a-0d32ff5296fb',
            'companyId': 'fcfc12fc-4ecf-46e2-a48f-ba5159f55908',
            'grantType': 1,
            'effectiveTime': '2019-08-15 00:00',
            'failureTime': '2019-09-05 12:00',
            'number': 10
        }
        self.result = r.post(
            company_resource.GRANT_RESOURCE_PROVIDER, data=data, headers=self.header)


if __name__ == "__main__":
    runTests([
        TestCompanyResource("test_grant_resource"),
        # TestCompanyResource("test_list")
    ])
