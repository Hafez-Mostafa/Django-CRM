import mysql.connector

# Establish a connection to the MySQL server
try:
    with mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            passwd='mosmoy12345',
            auth_plugin='mysql_native_password'
    ) as connection:

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Your SQL query to create the database
        query = "CREATE DATABASE IF NOT EXISTS mosmoy"

        # Execute the query
        cursor.execute(query)

        print('DATABASE CREATED SUCCESSFULLY')

except mysql.connector.Error as err:
    print(f"Error: {err}")
