import pymysql

# 创建连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='db6',
    port=3306,
    charset='utf8'
)
# 创建游标
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from tb1'
print(sql)

res = cur.execute(sql)
print(res)

# result = cur.fetchone()  1400245867
# print(result)
# result = cur.fetchone()
# print(result)

# result = cur.fetchmany(3)
#  负数表示从末尾往前的几位不显示
result = cur.fetchmany(-1)

# result = cur.fetchall()

print(result)

cur.close()
conn.close()