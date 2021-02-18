"""

Run a MySQL query and get information about its execution.

Example command line:

python runquery.py database hostname username password sqlscriptname

Arguments:

database - Name of the MySQL database that you want to use when you connect.
hostname - Name of the host that MySQL is running on.
username - Name of the MySQL user to login as
password - Password for username
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

"""

import mysql.connector
import time
import sys

if len(sys.argv) != 6:
    print("Usage: runquery.py database hostname username password sqlscriptname")
    sys.exit(-1)

dbname = sys.argv[1]
hostname = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
sqlscript = sys.argv[5]

with open(sqlscript, 'r') as sqlfile:
    query=sqlfile.read()

before_connect = time.time()

cnx = mysql.connector.connect(user=username, password=password,
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
