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
        company_id = '025c647c-9281-486f-8c72-2bf18a2c1f5d'
        order_no = ''
        effective_time = ''
        failure_time = ''
        start_time = '2019-08-26'
        end_time = '2019-08-28'

        url = Order.LIST + f'?page=1&pageSize=10&companyId={company_id}&orderNo={order_no}' \
            f'&effectiveTime={effective_time}&failureTime={failure_time}&startTime={start_time}&endTime={end_time}'
        self.result = self.r.get(url)

    def test_detail(self):
        """订单详情
        """
        order_id = '1bae2027-054f-4364-8015-ab8028c1c748'
        url = Order.DETAIL + f"{order_id}?page=1&pageSize=10"
        self.result = self.r.get(url)


if __name__ == "__main__":
    run_tests([
        # TestOrder("test_list"),
        TestOrder("test_detail")
    ])
