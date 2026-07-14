from connect_mysql import get_db_connection

mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
    print("Failed to connect to the database.")
    exit()

table_name = "products"
create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_name VARCHAR(255) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        stock_quantity INT DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""
try:
    cursor.execute(create_table_query)
    print(f"Table '{table_name}' created successfully.\n")

    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()
    print("Table structure:")

    for column in columns:
        print(column)

except Exception as e:
    print("Error creating table:", e)

finally:
    if cursor:
        cursor.close()
        print("\nCursor Closed.")

    if mysql_db and mysql_db.is_connected():
        mysql_db.close()
        print("Connection closed.")
