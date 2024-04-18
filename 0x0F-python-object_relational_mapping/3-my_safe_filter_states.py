#!/usr/bin/python3
"""
This script connects to a MySQL server
based on the provided state name.
The script takes four arguments: MySQL username, MySQL password,
database name, and state name searched (safe from MySQL injection).
Results are sorted in ascending order by states.id.

Usage:
    ./3-my_safe_filter_states.py <mysql_username> <mysql_password>
    <database_name> <state_name>

Example:
    ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
    (2, 'Arizona')
"""

import sys
import MySQLdb


def display_states(username, password, database, state_name):
    """
    Connects to a MySQL database and retrieves values from the states table
    based on the provided state name.
    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
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
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    mysql_password = sys.argv[2]
    mysql_username = sys.argv[1]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    display_states(mysql_username, mysql_password, database_name, state_name)
