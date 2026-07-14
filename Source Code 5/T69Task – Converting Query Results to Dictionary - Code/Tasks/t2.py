from connect_mysql import get_db_connection
mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
   print("Failed to connect to database")
   exit()

min_price = 5000
min_stock = 20

query = """SELECT * FROM products WHERE price > %s 
           AND stock_quantity < %s"""
cursor.execute(query, (min_price,min_stock))
products = cursor.fetchall()

print(f"\nProducts with price > ${min_price} "
      f"AND stock < {min_stock}:\n")

for product in products:
   print(f"ID: {product[0]} | "
         f"Name: {product[1]} | "
         f"Price: ${product[2]} | "
         f"Stock: {product[3]}"
        )

cursor.close()
mysql_db.close()
print("\nConnection Closed.")
