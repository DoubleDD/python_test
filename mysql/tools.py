# -*- coding:utf-8 -*-
import init_env
import pymysql


class DBConfig:
    host = "localhost"
    username = "root"
    password = "123456"
    schema = "test"


class DB:
    def __init__(self, config: DBConfig):
        self.db = pymysql.connect(
            config.host, config.username, config.password, config.schema)

    def execute(self, *sqls):
        print(sqls)
        if len(sqls) < 1:
            return

        result_list = []
        cursor = self.db.cursor()
        for sql in sqls:
            cursor.execute(sql)
            data = cursor.fetchall()
            result_list.append(data)
        return result_list

    def close(self):
        self.db.close()


if __name__ == "__main__":
    db = DB(DBConfig())

    db.execute("SELECT VERSION()")

    dropTable = "DROP TABLE IF EXISTS EMPLOYEE"
    createTable = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
    db.execute(dropTable, createTable)

    db.close()
