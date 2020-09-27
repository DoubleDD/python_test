# -*- coding:utf-8 -*-
import init_env

from unittest import TestCase
from common.HttpUtils import HttpUtils
from common.DateUtils import currentTimeMillis
from common.md5Utils import md5_sign
from common.base_test import run_tests


r = HttpUtils()
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer fc28da67-42f1-4a36-89d2-5ba1e05ac59e'
}


class RegisteredTest(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        result = self.result
        print("\n接口响应：")
        r.logJson(jsonStr=result.text)
        assert result.status_code == 200, "请求状态码应为 200"

    def test_device_install(self):
        """
        设备安装
        """
        # mock 参数
        data = {
            'id': '758938060460040192', # 设备ID
            'installUnit': '1', # 安装单位
            'installDate': '2020-09-27 13:52:23', # 安装日期
            'deviceFiles': [ # 文件上传列表
                {
                    'fileName': '安装方案',
                    'filePath': '文件url',
                    'fileType': '文件类型'
                }
            ],
            'operatorIds': [ # 安装人员ID列表
                '1111','2222','3333'
            ]
        }
        url = 'http://localhost:10003/machineDevice/installation'
        self.result = r.post(url=url, data=data, headers=headers)


if __name__ == "__main__":
    run_tests([
        RegisteredTest('test_device_install'),
    ])
