#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
The script takes four arguments.
It connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id.
Only one execute() statement is allowed.
Results must be displayed as they are in the example below.
"""

import sys
import MySQLdb


def list_cities(username, password, database, state_name):
    """
    Lists all cities of the given state from the specified database.
    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state.
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
        SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    result = cursor.fetchone()
    if result:
        print(result[0])
    else:
        print("No cities found for the state:", state_name)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    list_cities(mysql_username, mysql_password, database_name, state_name)
