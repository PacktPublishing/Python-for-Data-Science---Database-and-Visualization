from connect_mysql import get_db_connection

mysql_db, cursor = get_db_connection()

if mysql_db is None or cursor is None:
   print("Failed to connect to database")
   exit()

# print("Tables BEFORE drop:\n")
# cursor.execute("SHOW TABLES")
# tables = cursor.fetchall()
#
# for table in tables:
#     print(table[0])
print("Databases BEFORE drop:\n")

cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()

for db in databases:
    print(db[0])

drop_db_query = "DROP DATABASE IF EXISTS estore_py"

try:
    cursor.execute(drop_db_query)
    print(f"\nDatabase 'estore_py' dropped successfully.\n")

    print("Databases AFTER drop:\n")
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()

    for db in databases:
        print(db[0])

except Exception as e:
    print("Error while dropping table:", e)

finally:
    if cursor:
        cursor.close()
        print("\nCursor closed")
    if mysql_db and mysql_db.is_connected():
        mysql_db.close()
        print("Connection closed")

