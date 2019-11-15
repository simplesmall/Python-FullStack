import pymysql

# 用 pymysql 去替换掉  MySQLdb() 解决 Error loading  MySQLdb module错误
pymysql.install_as_MySQLdb()
