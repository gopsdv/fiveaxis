import mysql.connector
import os
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

config = {
    "host": os.getenv("DBHOST"),
    "user": os.getenv("DBUSER"),
    "password": os.getenv("DBPASS"),
    "database": os.getenv("DBNAME"),
}

connection = mysql.connector.connect(**config)
if connection.is_connected():
    print("Connected to the database")

def run_query(query_type, query, params=None):
    try:
        cursor = connection.cursor(buffered=True)

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()

        if query_type == "SELECT":
            return cursor.fetchall()
        elif query_type == "INSERT" or query_type == "UPDATE":
            return cursor.lastrowid
        else:
            return None

    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed")


def run_bulk_query(query_type, query, params=None):
    try:
        cursor = connection.cursor(buffered=True)

        if params:
            cursor.executemany(query, params)
        else:
            cursor.executemany(query)
        connection.commit()

        if query_type == "SELECT":
            return cursor.fetchall()
        elif query_type == "INSERT" or query_type == "UPDATE":
            return cursor.lastrowid
        else:
            return None

    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed")


# if __name__ == "__main__":
#     formated_param([{{"name": "foo"}}])
