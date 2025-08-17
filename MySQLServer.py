import mysql.connector
from mysql.connector import errorcode

# Database connection 
DB_HOST = "localhost"
DB_USER = "root"  
DB_PASSWORD = "mycountryKenya254" 

def create_database():
    cnx = None
    cursor = None

    try:
        cnx = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = cnx.cursor()

        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        cursor.execute(create_db_query)

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        else:
            print(f"Error: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if cnx is not None and cnx.is_connected():
            cnx.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()