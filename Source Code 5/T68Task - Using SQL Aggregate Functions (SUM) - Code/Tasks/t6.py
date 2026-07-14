from connect_mysql import get_db_connection
mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
  print("Failed to connect to database")
  exit()

min_price = 500
max_price = 2000

query = """SELECT product_name, price, stock_quantity 
           FROM products
           WHERE price BETWEEN %s AND %s"""

cursor.execute(query, (min_price, max_price))
products = cursor.fetchall()
print(f"\nProducts with price between ${min_price} and ${max_price}:\n")

for product in products:
  print(f"Name: {product[0]} | "
        f"Price: ${product[1]} | "
        f"Stock: {product[2]}"
       )

sum_query = """SELECT COALESCE(SUM(price), 0) AS total_cost
               FROM products
               WHERE price BETWEEN %s AND %s"""
cursor.execute(sum_query, (min_price, max_price))
result = cursor.fetchone()

print(f"\nTotal cost: ${result[0]}")

cursor.close()
mysql_db.close()
print("\nConnection closed")
