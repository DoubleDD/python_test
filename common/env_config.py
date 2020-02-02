# -*— coding: utf-8 -*-


class ServerCC:
    DEV = 2
    TEST = 3
    RASDEV = 4
    RASTEST = 5

    def __rasdev(self):
        url = 'https://rasdev9.zhixueyun.com'
        auth_url = 'https://rasdev9.zhixueyun.com/oauth/api/v1/auth'
        return (url, auth_url)

    def __rastest(self):
        url = 'https://rastest9.zhixueyun.com'
        auth_url = 'https://rastest9.zhixueyun.com/oauth/api/v1/auth'
        return (url, auth_url)

    def __dev(self):
        url = 'https://dev9.zhixueyun.com'
        auth_url = 'https://dev9.zhixueyun.com/oauth/api/v1/auth'
        return (url, auth_url)

    def __test(self):
        url = 'https://test9.zhixueyun.com'
        auth_url = 'https://test9.zhixueyun.com/oauth/api/v1/auth'
        return (url, auth_url)


    def getEnv(self, env=1):
        if env == self.DEV:
            return self.__dev()
        elif env == self.TEST:
            return self.__test()
        elif env == self.RASDEV:
            return self.__rasdev()
        elif env == self.RASTEST:
            return self.__rastest()
