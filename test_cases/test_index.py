# -*- coding:utf-8 -*-
from init_env import BASE_DIR
from common.HttpUtils import HttpUtils
from common.constains import index
from test_cases.base_test import runTests
import unittest


class TestIndex(unittest.TestCase):
    '''indexController中各个方法的测试用例
    '''

    def setUp(self):
        '''
        测试用例初始化操作
        '''
        self.r = HttpUtils()
        self.files = {'file': open(BASE_DIR+'/resouces/test.txt', 'rb')}
        self.data = {
            'id': '61e04cca-9213-451b-94ae-8d4dc2a1a5ea',
            'height': 300,
            'width': 300
        }

    def tearDown(self):
        '''
        执行结束恢复环境
        '''
        pass

    def test_fastdfsTest(self):
        response = self.r.post(index.fastdfsTest, files=self.files)
        assert response.status_code == 200

    def test_ossTest(self):
        response = self.r.post(index.ossTest, files=self.files, data=self.data)
        assert response.status_code == 200, ''

    def test_imageTest(self):
        result = self.r.post(index.image, data=self.data)
        self.r.logJson(jsonObj=result.json())
        assert result.status_code == 200


if __name__ == '__main__':
    tests = [
        TestIndex('test_fastdfsTest'),
        TestIndex('test_ossTest'),
        TestIndex('test_imageTest')
    ]
    runTests(tests)
