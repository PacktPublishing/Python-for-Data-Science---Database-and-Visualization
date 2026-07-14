from connect_mysql import get_db_connection
mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
   print("Failed to connect to database")
   exit()

query = """SELECT id, product_name, price, stock_quantity 
           FROM products LIMIT 5"""
cursor.execute(query)
products = cursor.fetchall()

print(f"\nProducts:")
for product in products:
   print(f"ID: {product['id']} | "
         f"Name: {product['product_name']} | "
         f"Price: ${product['price']} | "
         f"Stock: {product['stock_quantity']}"
         )

cursor.close()
mysql_db.close()
print("\nConnection closed")
