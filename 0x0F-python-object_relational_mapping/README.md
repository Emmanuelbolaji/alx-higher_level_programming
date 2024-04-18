0x0F Python - Object Relational Mapping (ORM)
Description
This directory contains projects and exercises related to Object Relational Mapping (ORM) in Python. ORM is a technique for accessing and manipulating a relational database using an object-oriented programming language. In these projects, we explore various ORM libraries and concepts in Python, such as SQLAlchemy and MySQLdb, to interact with databases and perform CRUD (Create, Read, Update, Delete) operations.

Projects
0-select_states.py: Script that connects to a MySQL server and selects all states from a specific database.
1-filter_states.py: Script that connects to a MySQL server and selects states whose name starts with a specified letter.
2-my_filter_states.py: Script that connects to a MySQL server and selects states based on user input, safely preventing SQL injection attacks.
3-my_safe_filter_states.py: Enhanced version of 2-my_filter_states.py with improved security against SQL injection attacks.
4-cities_by_state.py: Script that connects to a MySQL server and selects all cities from a specific database ordered by city id.
5-filter_cities.py: Script that connects to a MySQL server and selects cities based on user input, safely preventing SQL injection attacks.
model_city.py: Python class definition for City model to be used with SQLAlchemy.
model_state.py: Python class definition for State model to be used with SQLAlchemy.
6-model_state.py: Script that creates a State model in SQLAlchemy and connects to a MySQL server to display all State objects.
7-model_state_fetch_all.py: Script that connects to a MySQL server and prints all State objects from the database hbtn_0e_6_usa.
8-model_state_fetch_first.py: Script that connects to a MySQL server and prints the first State object from the database hbtn_0e_6_usa.
9-model_state_filter_a.py: Script that connects to a MySQL server and prints all State objects containing the letter 'a' from the database hbtn_0e_6_usa.
10-model_state_my_get.py: Script that connects to a MySQL server and prints the State object with the name passed as an argument from the database hbtn_0e_6_usa.
11-model_state_insert.py: Script that connects to a MySQL server and adds a new State object to the database hbtn_0e_6_usa.
12-model_state_update_id_2.py: Script that connects to a MySQL server and updates the name of the State object with id = 2 to 'New Mexico'.
13-model_state_delete_a.py: Script that connects to a MySQL server and deletes all State objects containing the letter 'a' from the database hbtn_0e_6_usa.
model_state.py: Updated Python class definition for State model to be used with SQLAlchemy.
relationship_city.py: Python class definition for City model with relationship to State model to be used with SQLAlchemy.
relationship_state.py: Updated Python class definition for State model with relationship to City model to be used with SQLAlchemy.
100-relationship_states_cities.py: Script that creates a State and City models with a one-to-many relationship using SQLAlchemy.
101-relationship_states_cities_list.py: Script that creates a State and City models with a one-to-many relationship using SQLAlchemy, and adds, commits, and lists all City objects linked to a State object from the database.
102-relationship_cities_delete.py: Script that deletes all City objects linked to a State object from the database using SQLAlchemy.
103-relationship_states.py: Script that creates a State and City models with a one-to-many relationship using SQLAlchemy, and prints all State objects with their corresponding City objects.
Author
Osundiraan Omobolaji
