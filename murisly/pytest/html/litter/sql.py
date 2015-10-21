#coding=utf8
import pymysql

def sqltest():
    try:
        conn = pymysql.connect(host = 'localhost', user = 'root', passwd = 'east', db = 'spider', port=3306)
        cur = conn.cursor()

        sql = 'insert alluser values(3, "测试")'
        cur.execute(sql)

        conn.commit()
        cur.close()
        conn.close()

    except Exception:
        print("exception...")
