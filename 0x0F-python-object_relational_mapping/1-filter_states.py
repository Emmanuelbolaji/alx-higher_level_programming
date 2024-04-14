#!/usr/bin/python3
"""
Script to list all states with a name starting with 'N' from a MySQL database.

This script connects to a MySQL server and retrieves states whose names start with 'N'
from a specific database.
The script takes three arguments: MySQL username, MySQL password, and database name.
Results are sorted in ascending order by states.id.

Usage:
    ./1-filter_states.py <username> <password> <database_name>

Example:
    ./1-filter_states.py root root hbtn_0e_0_usa

Output:
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
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)

    db.close()

if __name__ == "__main__":
    main()

