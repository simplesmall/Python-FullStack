# 创建表结构
import pymysql

# 连接数据库
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    db='web'
)
# 创建游标
cur = conn.cursor()
sql = '''
    create table userinfo(
    id int primary key auto_increment,
    name varchar(20),
    password varchar(20)
    )
'''
cur.execute(sql)
conn.commit()
cur.close()
conn.close()
