# -*- coding:utf-8 -*-
import requests as r
import unittest
import json
import demjson


class HttpUtils:
    def post(self, url=None, files=None, data=None, headers=None):
        """http post请求

        Keyword Arguments:
            url {[type]} -- [description] (default: {None})
            files {[type]} -- [description] (default: {None})
            data {[type]} -- [description] (default: {None})
            headers {[type]} -- [description] (default: {None})

        Returns:
            response -- [description]
        """
        print("\n-------------------------------------------------------")
        print("\n请求url：\n"+url)
        print("\n请求数据：")
        self.logJson(jsonObj=data)
        if not 'Content-Type' in headers.keys():
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        response = r.post(url=url, data=demjson.encode(data), files=files, headers=headers)
        print("响应数据：")
        self.logJson(jsonStr=response.text)
        return response

    def get(self, url, headers=None):
        print("请求url：\n"+url)
        # 设置编码

        response = r.get(url, headers=headers)
        return response

    def toJsonString(self, obj):
        return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False)

    def fromJsonString(self, text):
        return json.loads(text)

    def logJson(self, jsonStr=None, jsonObj=None):
        if jsonStr != None:
            jsonObj = self.fromJsonString(jsonStr)

        print(self.toJsonString(jsonObj))


if __name__ == '__main__':
    run = HttpUtils()
    dic = {'key1': 'value1', 'abc': '123'}
    str = '[{"id":"f35dcffc-28c1-484a-839b-25ee1ebb90dc","createTime":1564573635044,"filename":"plant.jpg","contentType":"image/jpeg","extention":null,"path":"default/M00/01/7C/cjeztl1Bf6-AURJEAAD2XHGL_5A181.jpg","size":63068,"translateId":null,"translateFlag":null,"translateLevel":null,"duration":null,"thumbStatus":null,"thumbPath":null,"configId":"default","fileKey":null,"thumbnailId":"5ea9209c-5672-40b9-bac8-12276db9702f","thumbnailPath":"default/M00/01/7C/cjeztl1Bf7qAXK9CAABzPksfsfU946.jpg","thumbnailImg":null,"fileOrder":null,"startOrEndFlag":null,"fastdfsPath":null,"uploadStatus":null}]'
    print(run.toJsonString(dic))
    jsonObj = run.fromJsonString(str)
    print(run.toJsonString(jsonObj))
