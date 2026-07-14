from connect_mysql import get_db_connection

mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
    print("Failed to connect to the database.")
    exit()

insert_query = """
    INSERT INTO products (product_name, price, stock_quantity) 
    VALUES (%s, %s, %s)
"""
product_data = (
    "Wireless Mouse",
    799.00,
    50
)

try:
    cursor.execute(insert_query, product_data)
    mysql_db.commit()
    print("Record inserted successfully.")

except Exception as e:
    print("Error while inserting record:", e)
    mysql_db.rollback()

finally:
    if cursor:
        cursor.close()
        print("\nCursor closed")
    if mysql_db and mysql_db.is_connected():
        mysql_db.close()
        print("Connection closed")

