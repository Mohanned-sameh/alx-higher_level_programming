#!/usr/bin/python3
import MySQLdb
from sys import argv

"""
script that lists all states with a name starting with N (upper N)
"""
if __name__ == "__main__":
    """
    connect to the database
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    """
    create a cursor object
    """
    cur = db.cursor()
    """
    execute the query
    """
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    """
    fetch the results
    """
    rows = cur.fetchall()
    """
    print the results
    """
    for row in rows:
        print(row)
    """
    close the cursor and database connection
    """
    cur.close()
    db.close()
