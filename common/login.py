# -*- conding:utf-8 -*-
from init_env import BASE_DIR
from common.HttpUtils import HttpUtils
from common.env_config import ServerCC
from common.DateUtils import currentTimeMillis, DateTime
import json
import os


token_json_path = BASE_DIR + '/resouces/token.json'

"""
获取接口调用凭证token工具
"""
URL_AUTH = 'https://rasdev9.zhixueyun.com/oauth/api/v1/auth'


def login(url=URL_AUTH, data=None):
    if data is None:
        return None

    r = HttpUtils()
    result = r.post(url, data=data)
    if result.status_code != 200:
        print('获取token失败')
        os._exit(0)
    token_file = open(token_json_path, 'w')
    jsonObj = json.loads(result.text)
    expires_in = jsonObj['expires_in']
    # 过期时间
    out_of_time = currentTimeMillis()+expires_in
    jsonObj['out_of_time'] = out_of_time
    jsonObj['expires_time'] = DateTime(out_of_time)
    jsonObj['create_time'] = DateTime()
    jsonStr = json.dumps(jsonObj)
    token_file.write(jsonStr)
    token_file.close()
    return jsonStr


def getToken(url=URL_AUTH, data=None, content=None):
    if content == '' or content == None:
        token_file = open(token_json_path, 'r')
        content = token_file.read()
        token_file.close()

    if content == '' or content == None:
        content = login(url, data)
        return getToken(url, content)

    jsonObj = json.loads(content)
    access_token = jsonObj['access_token']
    token_type = jsonObj['token_type']
    out_of_time = jsonObj['out_of_time']

    if out_of_time < currentTimeMillis()+5:
        content = login(url, data)
        return getToken(url, content)

    token = token_type+'__'+access_token
    return token


if __name__ == "__main__":
    server = ServerCC()
    URL_AUTH = server.getEnv(ServerCC.DEV)[1]
    # print(getToken(''))
    login(URL_AUTH)
