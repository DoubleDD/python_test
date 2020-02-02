# -*- coding:utf-8 -*-
import init_env

from urls import Registered, APIKEY, SECRET
from unittest import TestCase
from common.HttpUtils import HttpUtils
from common.DateUtils import currentTimeMillis
from common.md5Utils import md5_sign
from common.base_test import run_tests


r = HttpUtils()


class RegisteredTest(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        result = self.result
        print("\n接口响应：")
        r.logJson(jsonStr=result.text)
        assert result.status_code == 200, "请求状态码应为 200"

    def test_auth_register(self):
        """
        自动注册
        """
        # mock 参数
        data = {
            'token': 'd9888b78d199fb4c9e9b38d2b0c192d7',
            'organizationId': 1
        }
        # data['sign'] = md5_sign(data, SECRET)
        url = Registered.AUTH_REGISTER
        self.result = r.post(url=url,data=data)


if __name__ == "__main__":
     run_tests([
        RegisteredTest('test_auth_register'),
    ])
