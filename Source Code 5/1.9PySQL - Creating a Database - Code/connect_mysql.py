import mysql.connector
from mysql.connector import Error

mysql_db = None
cursor = None

try:
   mysql_db = mysql.connector.connect(
       host="localhost",
       user="root",
       password=""
   )

   if mysql_db.is_connected():
       print("Connected to MySQL!\n")
       cursor = mysql_db.cursor()
       db_name = "estore_py"

       try:
           cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
           print(f"Database '{db_name}' created successfully.")
       except Error as e:
           print("Error while creating database:", e)

except Error as e:
   print("Error while connecting:", e)

finally:
   if cursor is not None:
       cursor.close()
       print("\nCursor closed")

   if mysql_db is not None and mysql_db.is_connected():
       mysql_db.close()
       print("Connection closed")
