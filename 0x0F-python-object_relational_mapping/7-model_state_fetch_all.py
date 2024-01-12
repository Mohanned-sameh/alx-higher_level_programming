#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connects to database
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    # cur to talk with the database
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # fetch data
    rows = cur.fetchall()
    # prints rows
    for row in rows:
        print(row)
    # close connection
    cur.close()
    db.close()
