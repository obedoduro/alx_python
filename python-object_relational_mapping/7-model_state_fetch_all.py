import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_states(username, password, database_name):
    # Create a SQLAlchemy engine to connect to the MySQL server
    engine = create_engine("mysql://{username}:{password}"
                           "@localhost:3306/{database_name}")

    # Create a session to interact with the database
    session = Session(engine)

    try:
        # Query and list all State objects sorted by states.id
        states = session.query(State).order_by(State.id).all()

        # Display the results
        for state in states:
            print(f"{state.id}: {state.name}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the session and engine
        session.close()
        engine.dispose()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states(username, password, database_name)
