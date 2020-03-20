import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(user='root',host='localhost',password='',database='movies')
    sql_select_query = "select * from detail"
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    print(cursor.execute)

except Error as e:
    print("blablbabla")

finally:
    if(connection.is_connected()):
        connection.close()
        cursor.close()
        print("conection is closed")