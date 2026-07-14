from connect_mysql import get_db_connection
import csv
mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
 print("Failed to connect to database")
 exit()

query = """SELECT id, product_name, price, stock_quantity
           FROM products 
           ORDER BY price DESC 
           LIMIT 5"""

cursor.execute(query)
products = cursor.fetchall()

filename = "products_data.csv"
with open(filename, mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Product Name', 'Price(in USD)', 'Stock Quantity'])

    for product in products:
        writer.writerow([product["id"], product["product_name"], float(product["price"]), product["stock_quantity"]])

print(f"\nData exported successfully to '{filename}'")


cursor.close()
mysql_db.close()
print("Connection closed")
