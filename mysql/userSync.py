# -*- coding:utf-8 -*-
import init_env
import base64
import urllib
from mysql.tools import DB, DBConfig
from common.HttpUtils import HttpUtils


class UserInfo:
    def __init__(self):
        self.id = ''
        self.username = ''
        self.id_card = ''
        self.mobile = ''
        self.email = ''

    def parse(self, row):
        self.id = row[0]
        self.username = row[1]
        self.id_card = row[2]
        self.mobile = row[3]
        self.email = row[4]
        return self


r = HttpUtils()


def base64Str(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


class Mimayun:
    def __init__(self):
        self.app_url = 'http://111.203.206.158:18083'
        self.app_id = 17

    def getSign(self, id):
        originMsg = "appId=%s&id=%s" % (self.app_id, id)
        return base64Str(originMsg)

    def userRegister(self, userInfo: UserInfo):
        """
        注册用户
        """
        data = {
            'appId': self.app_id,
            'id': userInfo.id,
            'userName': userInfo.username,
            'idNoType': 1,
            'idNo': userInfo.id_card,
            'telephone': userInfo.mobile,
            'isCheckTime': 2,
            'email': userInfo.email
        }
        data['sign'] = self.getSign(userInfo.id)
        url = "%s/openapi/v1/user/register" % self.app_url
        result = r.post(url=url, data=data)
        return result


def sync():
    dbConfig = DBConfig()
    dbConfig.host = '172.30.1.216'
    dbConfig.username = 'gansu_dev'
    dbConfig.password = '1qazWSX_gansu'
    dbConfig.schema = 'mid_usercenter'

    db = DB(dbConfig)

    # 查询有身份证的用户
    sql = '''
    select id,username,id_card,tel_mobile,email
    from yl_auth_user
    where id_card != '' and tel_mobile != ''
    '''

    result = db.execute(sql)[0]

    for row in result:
        user = UserInfo().parse(row)
        result = Mimayun().userRegister(user)
        print(urllib.parse.unquote(result.text))

    db.close()

if __name__ == "__main__":
    sync()
