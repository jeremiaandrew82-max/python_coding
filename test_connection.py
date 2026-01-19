import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="testdb"
)

print("Connected!")

conn.close()