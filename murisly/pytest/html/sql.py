import pymysql

try:
    conn=pymysql.connect(host='localhost',user='root',passwd='sm%198809',db='test',port=3306)
    cur=conn.cursor()

    cur.execute('insert info values(3, "lily")');

    cur.execute('select * from info')
    ret = cur.fetchall();

    for r in ret:
        print(r);

    conn.commit();
    cur.close()
    conn.close()
except Exception:
    print("exception...");
