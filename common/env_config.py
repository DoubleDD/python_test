# -*— coding: utf-8 -*-


class ServerCC:
    LOCAL = 1
    DEV = 2

    def __local(self):
        url = 'http://localhost:8888'
        auth_url = 'https://rasdev9.zhixueyun.com/oauth/api/v1/auth'
        return (url, auth_url)

    def __dev(self):
        url = 'https://rasdev9.zhixueyun.com'
        auth_url = 'https://rasdev9.zhixueyun.com/oauth/api/v1/auth'
        return (url, auth_url)

    def getEnv(self, env=1):
        if env == self.LOCAL:
            return self.__local()
        elif env == self.DEV:
            return self.__dev()
        else:
            return self.__local()
