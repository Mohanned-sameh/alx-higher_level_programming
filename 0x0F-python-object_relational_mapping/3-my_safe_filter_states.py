#!/usr/bin/python3
import MySQLdb
from sys import argv

"""
script that takes in arguments and
 displays all values in the states table of hbtn_0e_0_usa
 where name matches the argument. But this time,
 write one that is safe from MySQL injections!
"""
if __name__ == "__main__":
    # creates a connection to the database
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    # creates a cursor object
    cur = db.cursor()
    # executes a query to retrieve data from the states table
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", (argv[4],))
    # fetches all rows from the query result
    rows = cur.fetchall()
    # prints each row
    for row in rows:
        print(row)
    # closes the cursor and database connection
    cur.close()
    db.close()
