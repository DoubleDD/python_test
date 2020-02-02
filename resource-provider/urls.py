# -*- coding:utf-8 -*-
import init_env

from url_tools import build_url

APIKEY = '1afdc343c61a837225d1d2cbd2398c90'
SECRET = 'e99f26da39f81e9cd30be44b35c80c72'


class Registered:
    context = "/api/v1/security-center"
    AUTH_REGISTER = build_url(context + '/auth-registered')
    REGISTER = build_url(context + '/registered')
