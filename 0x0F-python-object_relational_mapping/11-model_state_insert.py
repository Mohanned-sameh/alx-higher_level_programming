#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    # creates engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(engine)
    # binds sessions
    Session = sessionmaker(bind=engine)
    session = Session()
    # adds new state to database
    new_state = State(name="Louisiana")
    session.add(new_state)
    # commit changes
    session.commit()
    # prints new state
    print(new_state.id)
    # closses session
    session.close()
