# -*- coding:utf-8 -*-
import init_env
import time


class Order:
    """创建订单
    """
    def __init__(self, driver=None):
        self.driver = driver
        # 1.创建订单
        self.create()
        # 2.提交订单并生效
        self.active()

    def create(self):
        """创建订单
        """
        print('创建订单')

        time.sleep(5)
        pass

    def active(self):
        """提交订单并生效
        """
        print('提交订单并生效')

        time.sleep(5)
        pass
