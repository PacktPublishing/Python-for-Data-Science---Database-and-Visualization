from connect_mysql import get_db_connection
mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
   print("Failed to connect to database")
   exit()

min_stock = 20
max_stock = 50

query = """SELECT * FROM products 
           WHERE stock_quantity BETWEEN %s AND %s 
           ORDER BY stock_quantity ASC"""

cursor.execute(query, (min_stock, max_stock))
products = cursor.fetchall()

print(f"\nProducts with stock between {min_stock} "
      f"and {max_stock}:\n")

for product in products:
   print(f"ID: {product[0]} | "
         f"Name: {product[1]} | "
         f"Price: ${product[2]} | "
         f"Stock: {product[3]}"
        )

cursor.close()
mysql_db.close()
print("\nConnection closed")
