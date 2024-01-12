#!/usr/bin/python3
"""
prints all City object from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # creates engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    # binds engine to sessions
    Session = sessionmaker(bind=engine)
    session = Session()
    # query to print city and states
    for city, state in (
        session.query(City, State).filter(City.state_id == State.id).order_by(City.id)
    ):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    # closses connections
    session.close()
    engine.dispose()
