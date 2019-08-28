#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from unittest import TestCase

import init_env
from common.base_test import run_tests
from common.cc import build_url
from common.HttpUtils import HttpUtils


r = HttpUtils()


class TestExport(TestCase):
    def tearDown(self):
        file_dir = init_env.BASE_DIR+'/download/order/'
        # 判断文件夹是否存在，不存在则创建
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        filePath = file_dir + self.fileName
        with open(filePath, "wb") as file:
            file.write(self.result.content)

        # 调用系统程序打开文件
        os.startfile(filePath)

    def test_order_export(self):
        """订单导出测试

        https://rastest9.zhixueyun.com/api/v1/content/order/export?orderIds=&companyId=4d6d985a-0d7d-4cb8-9957-af1cbd056ee4
        """
        order_ids = ''
        company_id = '4d6d985a-0d7d-4cb8-9957-af1cbd056ee4'
        url = build_url(
            f'/order/export?orderIds={order_ids}&companyId={company_id}')
        self.result = r.get(url)
        self.fileName = f'order_{company_id}.xlsx'

    def test_order_detail_export(self):
        """订单详情（课程清单）导出测试

        http://localhost:8888/api/v1/content/order/detail/1bae2027-054f-4364-8015-ab8028c1c748/export
        """
        order_id = '1bae2027-054f-4364-8015-ab8028c1c748'
        url = build_url(f'/order/detail/{order_id}/export')
        self.result = r.get(url)
        self.fileName = f'order_detail_{order_id}.xlsx'


if __name__ == "__main__":
    run_tests([
        TestExport('test_order_export'),
        TestExport('test_order_detail_export')
    ])
