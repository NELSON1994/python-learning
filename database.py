#!/usr/bin/python

import MySQLdb

# Open database connection
# ip,usern,password, dbname
db = MySQLdb.connect("172.17.0.2", "root", "Nel62*com", "mysqldbpython")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : ", data)

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

print("-----> creating the table in the database")
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

print("----> inserting data into the database")
sql1 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
try:
    print("----> executing the statement")
    cursor.execute(sql1)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

print("----> reading the data from database using a given query")
sql = "SELECT * FROM EMPLOYEE \
        WHERE INCOME > '%d'" % (1000)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    # fetchOne(),rowCount()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # Now print fetched result
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income))

except:
    print("Error: unable to fetch data")


print("-----> updating records")
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1"
#                           WHERE SEX = "'%c' % ('M')"

print("-----> delete operations here")
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
print("----> disconnecting the database connection")
db.close()
print("----> disconnection successful")



# Transactions are a mechanism that ensures data consistency. Transactions have the following four properties −
# Atomicity − Either a transaction completes or nothing happens at all.
# Consistency − A transaction must start in a consistent state and leave the system in a consistent state.
# Isolation − Intermediate results of a transaction are not visible outside the current transaction.
# Durability − Once a transaction was committed, the effects are persistent, even after a system failure.
