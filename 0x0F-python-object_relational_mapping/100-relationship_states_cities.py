#!/usr/bin/python3
"""
script that creates the State "California" with the City "San Francisco" from
the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    # creates engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    # binds engine with sessions
    Session = sessionmaker(bind=engine)
    session = Session()
    # creates state and links to city
    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)
    # adds city and state then commit changes then closses connection
    session.add(california)
    session.add(san_francisco)
    session.commit()
    session.close()
