#!/usr/bin/python3
"""
 Script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    # makes connection to the database
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    # creates a cursor object
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # fetches all rows of a query result and returns a list of tuples.
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
