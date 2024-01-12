#!/usr/bin/python3
"""
script that takes in the name of a state
as an argument and lists all cities of that state,
 using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # creates a connection to the database
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    # creates a cursor object to execute SQL queries on the database
    cur = db.cursor()
    # executes a SELECT query to retrieve all cities from the database
    cur.execute(
        "SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC",
        (argv[4],),
    )
    # fetches all rows from the cursor object and prints them to the console
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    # close the connction
    cur.close()
    db.close()
