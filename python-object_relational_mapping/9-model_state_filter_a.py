import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_states_with_letter_a(username, password, database_name):
    # Create a SQLAlchemy engine to connect to the MySQL server
    engine = create_engine(f"mysql://{username}:"
                           f"{password}"
                           f"@localhost:3306/"
                           f"{database_name}")

    # Create a session to interact with the database
    session = Session(engine)

    try:
        # Query State objects containing the
        # letter 'a' and sort them by states.id
        states_with_a = (session.query(State).filter(State.name.like('%a%'))
                         .order_by(State.id).all())

        # Display the results
        for state in states_with_a:
            print(f"{state.id}: {state.name}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the session and engine
        session.close()
        engine.dispose()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username>"
              "<password> <database_name>")
    else:
        username, password = sys.argv[1], sys.argv[2]
        database_name = sys.argv[3]
        list_states_with_letter_a(username, password, database_name)
