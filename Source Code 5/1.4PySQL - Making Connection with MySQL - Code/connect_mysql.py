import mysql.connector
from mysql.connector import Error


mysql_db = None


try:
   mysql_db = mysql.connector.connect(
       host="localhost",
       user="root",
       password=""
   )


   if mysql_db.is_connected():
       print("Successfully connected to MySQL!")
       print("Connection ID:", mysql_db.connection_id)


except Error as e:
   print("Error while connecting to MySQL:", e)


finally:
   if mysql_db is not None and mysql_db.is_connected():
       mysql_db.close()
       print("Connection closed.")

