import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='mysql',
                       db='coctails_base',
                       charset='utf8mb4')

cursor = conn.cursor()

