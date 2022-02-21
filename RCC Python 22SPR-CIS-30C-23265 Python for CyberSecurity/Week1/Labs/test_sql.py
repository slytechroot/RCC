import mysql.connector
mydb = mysql.connector.connect(
  host="192.168.1.125",
  user="victim",
  password="Password!"
)
print(mydb)