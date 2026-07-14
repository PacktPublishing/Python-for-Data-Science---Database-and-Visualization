from connect_mysql import get_db_connection

mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
   print("Failed to connect to database")
   exit()

print("Products BEFORE delete:\n")
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()

for product in products:
   print(product)

delete_query = """
   DELETE FROM products
   WHERE product_name = 'USB-C Charger'
"""

try:
   cursor.execute(delete_query)
   mysql_db.commit()
   print("\nRecord deleted successfully.\n")
   print("Products AFTER delete:\n")
   cursor.execute("SELECT * FROM products")
   updated_products = cursor.fetchall()

   for product in updated_products:
      print(product)

except Exception as e:
   print("Error while deleting record:", e)
   mysql_db.rollback()

finally:
   if cursor:
      cursor.close()
      print("\nCursor closed")
   if mysql_db and mysql_db.is_connected():
      mysql_db.close()
      print("Connection closed")

