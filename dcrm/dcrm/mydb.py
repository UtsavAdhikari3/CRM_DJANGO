import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS elderco")
print("Database created successfully.")
cursor.close()
connection.close()
