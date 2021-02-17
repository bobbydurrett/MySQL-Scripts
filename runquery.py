"""

Run a MySQL query and get information about its execution.

Example command line:

python runquery.py MYDB myhost "Mypassword" test.sql

Arguments:

dbname - Name of the MySQL database that you want to use when you connect.
hostname - Name of the host that MySQL is running on.
password - Password for the MYUSER user on this MySQL system.
sqlscriptname - Name of a text file containing the SELECT statement that we are going to run.

Output:

Prints out the query text and some information such as in this example:

Number of rows returned = 6762
Number of bytes returned = 1238750
Connect time = 0.44091200828552246 seconds
Execute time = 0.8958208560943604 seconds
Fetch time = 1.4707059860229492 seconds

The number of bytes returned is the number of bytes for all of the columns converted to character
strings using the str() function. This indicates how large the returned data is.

To run this on my laptop I had to install the MySQL Python connector like this:

pip install mysql-connector

I am running this version of Python on my laptop:

Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32

"""

import mysql.connector
import time
import sys

if len(sys.argv) != 5:
    print("Usage: runquery.py dbname hostname MYUSERpassword sqlscriptname")
    sys.exit(-1)

dbname = sys.argv[1]
hostname = sys.argv[2]
password = sys.argv[3]
sqlscript = sys.argv[4]

with open(sqlscript, 'r') as sqlfile:
    query=sqlfile.read()

before_connect = time.time()

cnx = mysql.connector.connect(user='MYUSER', password=password,
                              host=hostname,
                              database=dbname)
                              
after_connect = time.time()

cursor = cnx.cursor()

print(" ")
print("Query:")
print(" ")
print(query)
print(" ")

before_execute = time.time()

cursor.execute(query)

after_execute = time.time()

row_count = 0
byte_count = 0

for row in cursor:
    if row_count % 10000 == 0:
        print("Rows queried = "+str(row_count))
    row_count += 1
    for column in row:
        byte_count += len(str(column))

after_fetch = time.time()

connect_seconds = after_connect - before_connect
execute_seconds = after_execute - before_execute
fetch_seconds = after_fetch - after_execute

print("Number of rows returned = "+str(row_count))
print("Number of bytes returned = "+str(byte_count))
print("Connect time = "+str(connect_seconds)+" seconds")
print("Execute time = "+str(execute_seconds)+" seconds")
print("Fetch time = "+str(fetch_seconds)+" seconds")

cursor.close()
cnx.close()