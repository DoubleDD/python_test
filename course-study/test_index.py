# -*- coding:utf-8 -*-
from init_env import BASE_DIR
from unittest import TestCase
from common.base_test import run_tests
from common.HttpUtils import HttpUtils
from common.md5Utils import md5_sign
from common.paramTools import originParam, buildParams, buildPostData
from common.DateUtils import currentTimeMillis


class TestIndex(TestCase):
    """indexController中各个方法的测试用例
    """

    def setUp(self):
        """
        测试用例初始化操作
        """
        self.r = HttpUtils()
        self.files = {'file': open(BASE_DIR+'/resources/test.md', 'rb')}
        self.data = {
            'id': '61e04cca-9213-451b-94ae-8d4dc2a1a5ea',
            'height': 300,
            'width': 300
        }

    def tearDown(self):
        """
        执行结束恢复环境
        """
        pass

    def test_fastdfsTest(self):
        response = self.r.post('http://localhost:8086/api/v1/course-study/course-import/courses-import-template?FROM_PC=1&FROM_WECHAT=1&FROM_APP=1', files=self.files)
        assert response.status_code == 200



if __name__ == '__main__':
    run_tests([
        TestIndex('test_fastdfsTest'),
    ])
