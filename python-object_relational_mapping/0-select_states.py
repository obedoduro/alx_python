import sys
from sqlalchemy import create_engine, MetaData, Table

def list_states(username, password, database_name):
    """List all states from the hbtn_0e_0_usa database."""
    try:
        # Create a SQLAlchemy engine to connect to the database
        engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database_name}")

        # Create a SQLAlchemy metadata object
        metadata = MetaData()

        # Define the 'states' table
        states = Table('states', metadata, autoload=True, autoload_with=engine)

        # Retrieve states sorted by ID
        result = engine.execute(states.select().order_by(states.c.id))

        # Display the results
        for row in result:
            print(row)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        engine.dispose()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states(username, password, database_name)
