import pymysql
conn = pymysql.connect("localhost", 'pllee', 'lpl18205583127', 'pymysql')

cursor = conn.cursor()
cursor.execute('show tables')
