import mysql.connector

mysqldb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123456",
    database = "lib_sys"
)
mysql_cursor = mysqldb.cursor()

c_db = ("show databases")

mysql_cursor.execute(c_db)

for l in mysql_cursor:
    print(l)