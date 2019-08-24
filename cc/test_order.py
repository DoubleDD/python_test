# -*- coding:utf-8 -*-
import init_env
from unittest import TestCase

from common.base_test import run_tests
from common.cc import Order
from common.HttpUtils import HttpUtils


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

        company_id = '4e99d6ff-bb02-4343-b637-169194d81fa3'
        order_no = '1908221838213013752'
        effective_time = '2019-08-20 00:00'
        failure_time = '2019-08-30 00:00'
        start_time = '2019-08-10'
        end_time = '2019-08-30'

        url = Order.LIST + f'?page=1&pageSize=10&companyId={company_id}&orderNo={order_no}' \
            f'&effectiveTime={effective_time}&failureTime={failure_time}&startTime={start_time}&endTime={end_time}'
        self.result = self.r.get(url)

    def test_detail(self):
        """订单详情
        """
        order_id = '86f82a88-9cad-40ce-97c1-78e285bf1973'
        url = Order.DETAIL + f"{order_id}?page=1&pageSize=10"
        self.result = self.r.get(url)


if __name__ == "__main__":
    run_tests([
        TestOrder("test_list"),
        # TestOrder("test_detail")
    ])
