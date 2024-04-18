#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
The script takes three arguments
It connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id.
Only one execute() statement is allowed.
Results are displayed as they are in the example below.
"""

import sys
import MySQLdb


def list_cities(username, password, database):
    """
    Lists all cities from the specified database.
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
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    list_cities(mysql_username, mysql_password, database_name)
