# -*- coding:utf-8 -*-
from unittest import TestCase

from common.base_test import run_tests
from common.cc import Order
from common.HttpUtils import HttpUtils
from init_env import BASE_DIR


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
        companyId = 'fcfc12fc-4ecf-46e2-a48f-ba5159f55908'
        url = Order.LIST + "?page=1&pageSize=10&companyId="+companyId
        self.result = self.r.get(url)

    def test_detail(self):
        """订单详情
        """
        orderId = 'fc119be6-b0b0-48df-b0b7-f260b995c5b7'
        url = Order.DETAIL + orderId + "?page=1&pageSize=10"
        self.result = self.r.get(url)


if __name__ == "__main__":
    run_tests([
        # TestOrder("test_list"),
        TestOrder("test_detail")
    ])
