import mysql.connector
from mysql.connector import Error


def list_tables():
    try:
        connection = mysql.connector.connect(
            host='106.15.170.173',
            port=3306,
            user='cityark_user',
            password='cityark_pass',
            database='cityark'
        )

        if connection.is_connected():
            print("Connected to MySQL database 'cityark'")
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            print("Tables in 'cityark':")
            for table in tables:
                print(table[0])
        else:
            print("Failed to connect to MySQL.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    list_tables()
