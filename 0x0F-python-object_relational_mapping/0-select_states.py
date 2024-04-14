#!/usr/bin/python3
"""
Script to list all states from a MySQL database.

This script connects to a MySQL server
The script takes three arguments
Results are sorted in ascending order by states.id.

Usage:
    ./0-select_states.py root root hbtn_0e_0_usa

Output:
    (1, 'California')
    (2, 'Arizona')
    (3, 'Texas')
    (4, 'New York')
    (5, 'Nevada')
"""
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()


if __name__ == "__main__":
    main()
