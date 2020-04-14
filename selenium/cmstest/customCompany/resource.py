# -*- coding:utf-8 -*-
import init_env


class Resource:
    """客户方获取资源
    """

    def __init__(self, driver=None):
        self.driver = driver
        self.getResource()

    def getResource(self):
        """获取资源
        """
        print('获取资源')
        pass
