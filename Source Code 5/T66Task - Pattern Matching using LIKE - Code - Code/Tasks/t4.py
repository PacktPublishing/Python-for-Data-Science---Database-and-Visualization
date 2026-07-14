from connect_mysql import get_db_connection
mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
   print("Failed to connect to database")
   exit()

search_term = "Wireless"
pattern = f"%{search_term}%"

query = """SELECT * FROM products 
           WHERE product_name LIKE %s"""
cursor.execute(query, (pattern,))
products = cursor.fetchall()

print(f"\nProducts containing '{search_term}':\n")
for product in products:
  print(f"ID: {product[0]} | "
        f"Name: {product[1]} | "
        f"Price: ${product[2]} | "
        f"Stock: {product[3]}"
       )

cursor.close()
mysql_db.close()
print("\nConnection closed")
