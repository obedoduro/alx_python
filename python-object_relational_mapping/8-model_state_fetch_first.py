import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

def print_first_state(username, password, database_name):
    # Create a SQLAlchemy engine to connect to the MySQL server
    engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database_name}")

    # Create a session to interact with the database
    session = Session(engine)

    try:
        # Query the first State object based on states.id
        first_state = session.query(State).order_by(State.id).first()

        # Display the result or "Nothing" if the table is empty
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")

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
        print_first_state(username, password, database_name)
