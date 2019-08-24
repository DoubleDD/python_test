# -*- coding:utf-8 -*-
import init_env
from unittest import TestCase

from common.base_test import run_tests
from common.cc import CourseInfo
from common.HttpUtils import HttpUtils

r = HttpUtils()


class TestCourseInfo(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        result = self.result
        print("\n接口响应：")
        r.logJson(jsonStr=result.text)
        assert result.status_code == 200, "请求状态码应为 200"

    def test_course_info(self):
        """接入企业管理列表接口
        8e775e21-8f41-4411-87c7-95c1a0b9df6c/zz_BA2be9b031/f2cfcc86ce51104146066452959ec628
        """
        course_id = '8e775e21-8f41-4411-87c7-95c1a0b9df6c'
        org_code = 'zz_BA2783520f'
        token = 'f2cfcc86ce51104146066452959ec628'
        url = CourseInfo.AUTH + f'/{course_id}/{org_code}/{token}'
        self.result = r.get(url)


if __name__ == '__main__':
    run_tests([
        TestCourseInfo('test_course_info')
    ])
