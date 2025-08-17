import mysql.connector
from mysql.connector import errorcode

DB_HOST = "localhost"
DB_USER = "root"  
DB_PASSWORD = "mycountryKenya254"  
DATABASE_NAME = "alx_book_store"

def create_database():

    try:
        cnx = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = cnx.cursor()
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
        cursor.execute(create_db_query)

        print(f"Database '{DATABASE_NAME}' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'cnx' in locals() and cnx is not None and cnx.is_connected():
            cnx.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()