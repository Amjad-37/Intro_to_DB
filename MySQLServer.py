#!/usr/bin/python3
import mysql.connector

# Define your database connection parameters
# IMPORTANT: Replace with your actual MySQL credentials
db_config = {
    'host': "localhost",
    'user': "your_username",     # Usually 'root' in ALX environment
    'password': "your_password"  # The password you set for MySQL
}

try:
    # Establish the connection to the MySQL server
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # SQL command to create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Ensure the connection is closed
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
