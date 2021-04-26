import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)
#使用pymysql代替mysqldb连接数据库
pymysql.install_as_MySQLdb()