#!/usr/bin/python3
"""This module lists all state objects from
from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4])

    check = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            check = True
            break
    if check is False:
        print("Not found")
