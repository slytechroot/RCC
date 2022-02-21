import mariadb
import sys

try:
    # connection parameters
    conn_params = {
        'user' : "root",
        'password' : "Redwood123#",
        'host' : "192.168.1.125",
        'port' : 3306,
        'database' : "lethallabdb"
    }

    # establish a connection
    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()
    
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
    
print(cursor)