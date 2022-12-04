#!/usr/bin/python3
"""This script lists all states
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities c \
                JOIN states s ON c.state_id=s.id \
                WHERE s.name=%s \
                ORDER BY c.id", (sys.argv[4],))
    [print(", ".join([city[0] for city in cur.fetchall()]))]
