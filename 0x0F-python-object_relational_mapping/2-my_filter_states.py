#!/usr/bin/python3
import MySQLdb
from sys import argv

"""
script that takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
if __name__ == "__main__":
    """
    connect to the database and get the states
    """
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    """
    initliaze a cursor
    """
    cur = db.cursor()
    """
    execute the query
    """
    nmestr = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(nmestr)
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
    close the connections
    """
    cur.close()
    db.close()
