# -*- conding:utf-8 -*-
from init_env import BASE_DIR
from common.HttpUtils import HttpUtils
from common.constains import base64Upload
from common.ContentType import mime
from common.login import getToken
from test_cases.base_test import runTests
import unittest
import os
import base64


class TestBase64(unittest.TestCase):
    """文件base64编码格式上传测试

    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        """测试用例初始化操作
        """
        self.r = HttpUtils()
        file = open(BASE_DIR+'/resources/plant.jpg', 'rb')
        filename = file.name
        suffix = os.path.splitext(filename)[1]
        contentType = mime[suffix]
        base64_str = base64.b64encode(file.read())
        self.data = {
            'trackerServerKey': 'default',
            'contentType': contentType,
            'fileName': filename,
            'body': base64_str,
            'cutSize': '300,300'
        }
        file.close()
        self.header = {'Authorization': getToken()}

    def tearDown(self):
        '用例执行完成的后置操作'
        pass

    def test_fastdfs(self):
        result = self.r.post(base64Upload.fastdfs,
                             data=self.data, headers=self.header)
        self.r.logJson(jsonObj=result.json())
        assert result.status_code == 200

    def test_oss(self):
        result = self.r.post(
            base64Upload.oss, data=self.data, headers=self.header)
        self.r.logJson(jsonObj=result.json())
        assert result.status_code == 200


if __name__ == '__main__':
    tests = [
        TestBase64('test_fastdfs'),
        TestBase64('test_oss')
    ]
    runTests(tests)
