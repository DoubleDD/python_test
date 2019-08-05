# -*- coding:utf-8 -*-

import time

ymdhms = '%Y-%m-%d %H:%M:%S'
ymd = '%Y-%m-%d'
hms = '%H:%M:%S'


def currentTimeMillis():
    """获取当前时间戳

    Returns:
        float -- 带两位小数的时间戳
    """
    return time.time()


def Date(Timestamp=None):
    """将时间戳格式化为日期
    格式：YYYY-mm-dd

    Keyword Arguments:
        Timestamp {[int/float]} -- [时间戳] (default: {None})
    """
    Timestamp = currentTimeMillis() if Timestamp is None else Timestamp
    return DateTimeFormat(ymd, Timestamp)


def Time(Timestamp=None):
    """将时间戳格式化为时分秒
    格式：HH:MM:ss

    Keyword Arguments:
        Timestamp {[type]} -- [description] (default: {None})
    """
    Timestamp = currentTimeMillis() if Timestamp is None else Timestamp
    return DateTimeFormat(hms, Timestamp)


def DateTime(Timestamp=None):
    """格式化为日期时间
    时间格式为 YYYY-mm-dd HH:MM:ss

    Keyword Arguments:
        Timestamp {float} -- 时间戳 (default: {None})
    """
    Timestamp = currentTimeMillis() if Timestamp is None else Timestamp
    return DateTimeFormat(ymdhms, Timestamp)


def DateTimeFormat(FormatStr=None, Timestamp=None):
    """格式化时间

    Keyword Arguments:
        FormatStr {string} -- [日期时间格式] (default: {None})
        Timestamp {int/float} -- [时间戳] (default: {None})
    """
    FormatStr = ymdhms if FormatStr is None else FormatStr
    Timestamp = currentTimeMillis() if Timestamp is None else Timestamp
    return time.strftime(FormatStr, time.localtime(Timestamp))
