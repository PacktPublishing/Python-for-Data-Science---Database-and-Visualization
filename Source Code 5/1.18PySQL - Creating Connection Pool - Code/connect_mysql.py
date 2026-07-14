import mysql.connector
from mysql.connector import Error, pooling

connection_pool = pooling.MySQLConnectionPool(
    pool_name='estore_pool',
    pool_size=5,
    pool_reset_session=True,
    host="localhost",
    user="root",
    password=""
)

def get_db_connection():
    try:
       mysql_db = connection_pool.get_connection()

       if mysql_db.is_connected():
           print("Connected to MySQL\n")
           cursor = mysql_db.cursor()

           db_name = "estore_py"
           cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
           print(f"Database '{db_name}' is ready.")

           cursor.execute(f"USE {db_name}")
           print(f"Now using database '{db_name}'.")

           return mysql_db, cursor

    except Error as e:
       print("Error while connecting:", e)
       return None, None


if __name__ == "__main__":
    mysql_db, cursor = get_db_connection()

    if mysql_db and cursor:
        print("Connection successful!")

        cursor.close()
        mysql_db.close()
        print("Connection closed")

# finally:
#    if cursor is not None:
#        cursor.close()
#        print("\nCursor closed")
#
#    if mysql_db is not None and mysql_db.is_connected():
#        mysql_db.close()
#        print("Connection closed")
