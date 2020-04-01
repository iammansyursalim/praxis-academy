import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='movies'
)

cursor = cnx.cursor()
sql = "SELECT * FROM detail"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)