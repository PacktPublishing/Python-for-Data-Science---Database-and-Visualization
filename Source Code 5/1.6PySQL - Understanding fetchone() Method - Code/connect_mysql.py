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
      cursor = mysql_db.cursor(buffered=True)
      res = cursor.execute("SHOW DATABASES")
      db_1 = cursor.fetchone()
      print("First Database:", db_1[0])
      db_2 = cursor.fetchone()
      print("Second Database:", db_2[0])

except Error as e:
  print("Error while connecting to MySQL:", e)

finally:
  if mysql_db is not None and mysql_db.is_connected():
      mysql_db.close()
      print("Connection closed.")
