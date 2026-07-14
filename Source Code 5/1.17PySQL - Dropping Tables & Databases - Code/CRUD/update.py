from connect_mysql import get_db_connection

mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
   print("Failed to connect to database")
   exit()

print("Products BEFORE update:\n")

cursor.execute("SELECT * FROM products")
products = cursor.fetchall()

for product in products:
   print(product)

update_query = """
   UPDATE products
   SET price = %s, stock_quantity = %s
   WHERE product_name = %s
"""
values = (749.00, 60, "Wireless Mouse")

try:
   cursor.execute(update_query, values)
   mysql_db.commit()
   print("\nRecord updated successfully.\n")
   print("Products AFTER update: \n")
   cursor.execute("SELECT * FROM products")
   updated_products = cursor.fetchall()

   for product in updated_products:
      print(product)

except Exception as e:
   print("Error while updating record:", e)
   mysql_db.rollback()

finally:
   if cursor:
      cursor.close()
      print("\nCursor closed")
   if mysql_db and mysql_db.is_connected():
      mysql_db.close()
      print("Connection closed")
