'''
4.	Identify a package that can be used for Python security. 
Provide description and information about the package and modules. 
'''

print('My program of choice is - MySQL MariaDB.')
print('A MariaDB database has been setup on my home Raspberry PI 2 for testing.')

'''
Python developers can connect to MariaDB Enterprise through a native MariaDB Connector. 
Using MariaDB Connector/Python you can connect to MariaDB Enterprise to use and administer 
databases from within your Python application. 
'''
#install MariaDB in your system: pip3 install mariadb
#module import
from sqlite3 import connect
import mariadb
import sys
import mysql.connector

#connect to MariaDB Platform
try:
    connection_param = mariadb.connect(
        user = "db_user",
        password = "db_user_password",              #password removed
        host = '192.168.x.x',
        port = 3306,
        database = 'mydatabase',
    )
except mariadb.Error as e:
    print(f"Error connecting to the MariaDB platform: {e}")
    sys.exit(1)

#get cursor
cursor = connection_param.cursor()
#connection = mariadb.connect(**connection_param)

#retrieving information 
some_name = "John@gg.com" 
cursor.execute("SELECT first_name,last_name FROM lethallabdb WHERE first_name=?",(some_name,)) 

for first_name, last_name in cursor: 
    print(f"First name: {first_name}, Last name: {last_name}")

'''
#Using the same execute() method with an INSERT statement, you can add rows to the table.
#insert information 
try: 
    cursor.execute("INSERT INTO Information (first_name,last_name) VALUES (?, ?)", ("Maria","DB")) 
except mariadb.Error as e: 
    print(f"Error: {e}")

connection.commit() 
print(f"Last Inserted ID: {cursor.lastrowid}")

connection.close()
'''