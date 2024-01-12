#!/usr/bin/python3
"""
script that deletes all State objects with a name
containing the letter a
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    # creates the engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    # query all states
    states = session.query(State).filter(State.name.like("%a%")).all()
    # delete all states
    for state in states:
        session.delete(state)
    # commit the changes
    session.commit()
    # close the session
    session.close()
