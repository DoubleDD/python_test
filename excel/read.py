import xlrd
import sys
import os
from os.path import abspath, dirname, join
import pymysql




def update(userDic = {}):
    # 打开数据库连接
    db = pymysql.connect(host="172.30.1.216",user="gansu_dev",password="1qazWSX_gansu",database="eco_multiplex_adaptersite")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("select id,realname,sort_num from yp_address_list limit 1000")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    try:
        for d in data:
            username = d[1]
            if username in userDic:
                update_sql = "update yp_address_list set sort_num = %s where realname='%s' " % \
                     (userDic.get(username, 999), username)
                print(update_sql)
                cursor.execute(update_sql)

        update_null_data = 'update yp_address_list set sort_num = 999 where sort_num is null'
        print(update_null_data                                                                                                                                                                                                                                                                                                                                                                                                               )
        cursor.execute(update_null_data)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()





if __name__ == '__main__':
    BASE_DIR = dirname(dirname(abspath(__file__)))
    xlsPath=os.path.join(BASE_DIR,'excel','username.xls')
    work_book = xlrd.open_workbook(xlsPath)
    sheet_2 = work_book.sheet_by_index(1)

    dic = {}
    for n in range(0,sheet_2.nrows):
        [sort_num,username] = sheet_2.row_values(n)
        dic[username.replace(' ','')] = int(sort_num)

    update(dic)

