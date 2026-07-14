from connect_mysql import get_db_connection
mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
  print("Failed to connect to database")
  exit()

query = """SELECT * FROM products 
           WHERE stock_quantity BETWEEN 20 AND 40 
           ORDER BY price ASC"""
cursor.execute(query)
products = cursor.fetchall()

print("\nProducts sorted by price (lowest to highest):\n")
for product in products:
  print(f"ID: {product[0]} | "
        f"Name: {product[1]} | "
        f"Price: ${product[2]} | "
        f"Stock: {product[3]}"
       )

cursor.close()
mysql_db.close()
print("\nConnection closed")
