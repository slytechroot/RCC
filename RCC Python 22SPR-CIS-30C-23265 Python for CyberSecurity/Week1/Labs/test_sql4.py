# import required modules
import mariadb
import sys
  
# establish connection to MySQL
connection = mariadb.connect(
    # specify host name
    host="192.168.1.125",
      
    # specify username
    user="root",
      
    # enter password for above user
    password="Redwood123#",
      
    # default port number for MySQL is 3306
    port=3306,
      
    # specify database name
    db="lethallabdb"
)
  
# make cursor for establish connection
mycursor = connection.cursor()
  
# display records before inserting
mycursor.execute("Select * from Information")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
  
      
# statement to insert record
mycursor.execute(
    "Insert into Information(firstname,lastname,gender,grade,dob,rollnumber) \
    select * from( Select 'Thomas','Main','m',30,2003-03-10, NULL) as temp \
    where not exists \
    (Select rollnumber from Information where rollnumber='2') LIMIT 1")
print("After inserting a record....")
  
  
# print records after insertion
mycursor.execute("Select * from Information")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
mycursor.execute("Commit")
  
  
# close connection
connection.close()