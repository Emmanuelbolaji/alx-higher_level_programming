#!/usr/bin/python3
"""
This script connects to MySQL server
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


def display_states(username, password, database, state_name):
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    state_name_bytes = state_name.encode('utf-8')
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_bytes,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    display_states(mysql_username, mysql_password, database_name, state_name)
