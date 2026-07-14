from connect_mysql import get_db_connection

mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
   print("Failed to connect to database")
   exit()

try:
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    print("\nAll Products:")
    for product in products:
        print(f"ID: {product[0]}")
        print(f"Name: {product[1]}")
        print(f"Price: ₹{product[2]}")
        print(f"Stock: {product[3]}")
        print(f"Created: {product[4]}")
        print("-" * 40)

except Exception as e:
    print("Error while reading products:", e)

finally:
    if cursor:
        cursor.close()
        print("\nCursor closed")
    if mysql_db and mysql_db.is_connected():
        mysql_db.close()
        print("Connection closed")

