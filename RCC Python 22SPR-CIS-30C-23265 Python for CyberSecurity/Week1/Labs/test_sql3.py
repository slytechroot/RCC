import mariadb
import sys

# Connect to MariaDB Platform
try:
    connection = mariadb.connect(
        user = "root",
        password = "Redwood123#",
        host = "192.168.1.125",
        port = 3306,
        database = "lethallabdb"

    )
    
    # Get Cursor
    cursor = connection.cursor()

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

print(cursor)