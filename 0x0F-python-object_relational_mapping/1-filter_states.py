#!/usr/bin/python3
"""This script lists all states
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states where name like 'N%' ORDER BY id")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
