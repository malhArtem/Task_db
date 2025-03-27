import sqlite3
# import pymysql
# import mysql-connector

# python get-pip.py

connect = sqlite3.connect("database.db")
# connect = pymysql.connect(host='localhost', 
#                             user="root", 
#                             password="password", 
#                             database="")

# cursor = connect.cursor()
# cursor = connect.cursor()
# cursor.execute("INSERT users(name=?, lastname=?)", (name, lastname))
# connect.commit()
# cursor.execute("SELECT * FROM users WHERE name=?", 
#                 (name,))

# result = cursor.fetchall() 
# result1 = cursor.fetchmany(10)
# result2 = cursor.fetchone()

# name = "Иван"

# print(f"Моё имя не {name}")
