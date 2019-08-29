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
        02c8b3d6-a9dd-4db4-8e33-bc9b0e3cfe79/zz_BA5904fe47
        """
        url = Test.AUTH + '/02c8b3d6-a9dd-4db4-8e33-bc9b0e3cfe79/zz_BA5904fe47'
        self.result = r.get(url)

if __name__ == "__main__":
    run_tests([
        TestTools('test_auth')
    ])
