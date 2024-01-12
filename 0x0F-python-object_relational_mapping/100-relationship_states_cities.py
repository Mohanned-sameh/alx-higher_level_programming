#!/usr/bin/python3
"""adds the State object “California”
with the City “San Francisco”
to the database hbtn_0e_100_usa"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import Table

if __name__ == "__main__":
    # creates engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    # binds sessions
    session = Session(engine)
    # new city
    new_city = City(name="San Francisco")
    # new state
    new = State(name="California")
    new.cities.append(new_city)
    # adds all
    session.add_all([new, new_city])
    # commits changes
    session.commit()
    # closses connections
    session.close()
