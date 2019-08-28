# -*- coding:utf-8 -*-
import init_env
from common.HttpUtils import HttpUtils
from common.cc import Test
from common.base_test import run_tests
from unittest import TestCase

# https://rastest9.zhixueyun.com/api/v1/content/test/auth/cd4ebc80-e06c-4f49-a980-bf9a137de848/zz_BA66e26fd6

r = HttpUtils()


class TestTools(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        result = self.result
        print("\n接口响应：")
        r.logJson(jsonStr=result.text)
        assert result.status_code == 200, "请求状态码应为 200"

    def test_auth(self):
        """课程授权测试
        8e775e21-8f41-4411-87c7-95c1a0b9df6c/zz_BA2be9b031
        """
        course_id = '8e775e21-8f41-4411-87c7-95c1a0b9df6c'
        org_code = 'zz_BA2783520f'
        url = Test.AUTH + f'/{course_id}/{org_code}'
        self.result = r.get(url)
