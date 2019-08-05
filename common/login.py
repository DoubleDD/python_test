# -*- conding:utf-8 -*-
from init_env import BASE_DIR
from common.HttpUtils import HttpUtils
from common.constains import URL_AUTH
from common.DateUtils import currentTimeMillis, DateTime
import json

token_json_path = BASE_DIR + '/resouces/token.json'

"""
获取接口调用凭证token
"""


def login():
    r = HttpUtils()
    data = {
        'key': 'oZImo5zozQggF2BymfTc090trJ3N6xyWfo18/8Lp7jTh8l2v5iCDg5phuOMsAthCWpnEJqsiMBtxMaMJ+1oBvaY4o9ONCHnNuQ636V9wYD1Ftmbv3NdKmFLxsfkrgBrVF/WUvct1jGnqISX9vYw6MWBhX9HBKGk2bwwMqxT33O8ol89KbhegEFtbIWAUE2T/AfjCXsMEJnI8gmMgCmO0Owf4eHseyLTGb6MAwZNkc/4=',
        'organization_id': 'N8XxZPBkHR4UcAuMtuMC4Q==',
        'login_method': 'JZNm+1f9txtGtiE0oRMJ1g==',
        'username': 'PjDD8fU4asbLJXaEbcNEwg==',
        'pword': '0GrD6MYSpX0BOZW15fev2w==',
        'captcha': ''
    }
    result = r.post(URL_AUTH, data=data)
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


def getToken(content=None):
    if content == '' or content == None:
        token_file = open(token_json_path, 'r')
        content = token_file.read()
        token_file.close()

    if content == '' or content == None:
        content = login()
        return getToken(content)

    jsonObj = json.loads(content)
    access_token = jsonObj['access_token']
    token_type = jsonObj['token_type']
    out_of_time = jsonObj['out_of_time']

    if out_of_time < currentTimeMillis()+5:
        content = login()
        return getToken(content)

    token = token_type+'__'+access_token
    return token


if __name__ == "__main__":
    # print(getToken(''))
    login()
