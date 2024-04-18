#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(name=sys.argv[4]).first()
    print(state.id if state else "Not found")
    session.close()
