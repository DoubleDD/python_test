# -*- coding:utf-8 -*-
import init_env

from ApiConfig import Api
from common.HttpUtils import HttpUtils
from threading import Timer


class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)


r = HttpUtils()
headers = {
    'Content-Type': 'application/json'
}


def ios():
    '''
    模拟ios设备
    '''
    headers['token'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50SWQiOiJHYW5zdURldl82ZWU2YjljMjZlNmZmMmExODA0MzAxNWI4YzUyMDM4NiIsInJhbmRvbSI6NjksImdyb3VwSWQiOiJHYW5zdURldl9kM2VlOWE4Y2ZiMWQ3Mjk4NzBiZTZhMjU3NzZjOWJmNSIsImFwcElkIjoiZ2Fuc3VfZGV2IiwidXNlcklkIjoiODhiNjQyOWIzOWZkMmQ4MzMxYWVmZDIxOWM2YjBjZWMiLCJ1dUlkIjoiZjRiZTM5YmJkZDIyNDkzOGE2NmU0NWE5MjNkNzFiOGQiLCJpYXQiOjE2MzAwNDcxODQsInVzZXJuYW1lIjoiYWRtaW4ifQ.n_U2u2NOtSZu77A_H323V6AHOhfSfDQb31-DCR9w688'
    r.post(url=Api.heartbeat, data={'device': 'ios', 'platform': 2}, headers=headers)


def android():
    '''
    模拟安卓设备
    '''
    headers['token'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50SWQiOiI0YjdkNjQ0ODQzMjg0M2Q1Yjg5NmIxMTViZjJjZGY1NCIsInJhbmRvbSI6NzgwLCJncm91cElkIjoiR2Fuc3VEZXZfZDNlZTlhOGNmYjFkNzI5ODcwYmU2YTI1Nzc2YzliZjUiLCJhcHBJZCI6ImdhbnN1X2RldiIsInVzZXJJZCI6IjkxZjdjNGZhOTU2YTFmNjA5Y2MxMThiNzZmNGYxNmE2IiwidXVJZCI6ImU1MjU3MjBiMjYzOTRiN2ZiYWJjZGY2NTVhZDY3ZjIzIiwiaWF0IjoxNjMwMDQ1NDQzLCJ1c2VybmFtZSI6InNqZ2wwMSJ9.7Cmgf8oFtT2c4GBIj_RBlsUWae10m3NEDwmX8gxlWt8'
    r.post(url=Api.heartbeat, data={"device": "android", "platform": 1}, headers=headers)


def app():
    ios()
    android()


if __name__ == "__main__":
    # t = RepeatingTimer(10.0, app)
    # t.start()
    ios()
