#!/usr/bin/python3
"""
This script connects to a MySQL server
The script takes four arguments
Results are sorted in ascending order by states.id.
usage:
    ./2-my_filter_states.py

Example:
    ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'

Output:
    (2, 'Arizona')
"""
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    for row in results:
        print(row)

    db.close()


if __name__ == "__main__":
    main()
