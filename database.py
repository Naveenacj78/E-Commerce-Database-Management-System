import mysql.connector
from mysql.connector import Error

def connect_db():

    try:

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Naveena@7592!",
            database="ecommerce_db"
        )

        if conn.is_connected():
            return conn

    except Error as e:

        print("Database Connection Error:")
        print(e)

        return None