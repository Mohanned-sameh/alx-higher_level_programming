#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # creates a connection to the database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )
    # creates a cursor object
    cur = conn.cursor()
    # executes a SELECT query to retrieve all cities from the database
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
                INNER JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC"
    )
    # fetches all rows from the cursor
    rows = cur.fetchall()
    # iterates through the rows and prints each city
    for row in rows:
        print(row)
    # closes the cursor and connection
    cur.close()
    conn.close()
