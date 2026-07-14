from connect_mysql import get_db_connection

mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
   print("Failed to connect to database")
   exit()

insert_query = """
   INSERT INTO products (product_name, price, stock_quantity)
   VALUES (%s, %s, %s)
"""
product_data = [
   ("Gaming Laptop", 55000.00, 10),
   ("Wireless Mouse", 799.00, 50),
   ("Mechanical Keyboard", 3499.00, 25),
   ("USB-C Charger", 1299.00, 40),
   ("Noise Cancelling Headphones", 5999.00, 15)
]

try:
   cursor.executemany(insert_query, product_data)
   mysql_db.commit()
   print("Records inserted successfully.")

except Exception as e:
   print("Error while inserting record:", e)
   mysql_db.rollback()

finally:
   if cursor:
       cursor.close()
       print("\nCursor closed")
   if mysql_db and mysql_db.is_connected():
       mysql_db.close()
       print("Connection closed")
