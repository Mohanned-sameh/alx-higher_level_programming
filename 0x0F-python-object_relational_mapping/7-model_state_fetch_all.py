#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    # creates engine to talk with database
    eng = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(eng)
    # binds session
    Session = sessionmaker(bind=eng)
    session = Session()
    # prints all states in database in ascending order by id.
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
