# -*- coding:utf-8 -*-
from init_env import BASE_DIR
from common.HttpUtils import HttpUtils
from common.cc import Order
from common.base_test import runTests
from unittest import TestCase


class TestOrder(TestCase):
    def setUp(self):
        self.r = HttpUtils()

    def tearDown(self):
        result = self.result
        self.r.logJson(jsonStr=result.text)
        assert result.status_code == 200, "请求状态码应为 200"

    def test_list(self):
        """订单列表接口
        """
        url = Order.list + "?page=1&pageSize=10"
        self.result = self.r.get(url)

    def test_detail(self):
        """订单详情
        """
        orderId = ''
        url = Order.detail + orderId + "?page=1&pageSize=10"
        self.result = self.r.get(url)


if __name__ == "__main__":
    runTests([
        # TestOrder("test_list"),
        TestOrder("test_detail")
    ])
