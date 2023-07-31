import tkinter as tk
import mysql.connector 

# Database credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "timothy69",
    "database": "local_lis"
}

try:
    # Connect to the MySQL database
    db_connection = mysql.connector.connect(**db_config)

    # Create a cursor object to execute SQL queries
    cursor = db_connection.cursor()

    # If the connection is successful, print a success message
    print("Successfully connected to the database!")

    # Close the cursor and database connection
    cursor.close()
    db_connection.close()

except mysql.connector.Error as error:
    # If an exception is raised, print the error message
    print(f"Error connecting to the database: {error}")

