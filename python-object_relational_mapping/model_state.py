from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Creating a State class inherting a Base
class State(Base):
    """
    Represents a state in a database.

    Attributes:
        id (int): An auto-generated unique identifier for the state.
                name (str): The name of the state with 
                a maximum length of 128 characters.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)


# Example usage of creating tables:
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    # Replace 'your_username', 'your_password',
    # and 'your_database' with your MySQL credentials
    # and database name
    engine = create_engine(
        'mysql://your_username:your_password@localhost:3306/your_database')

    # Create tables based on defined classes
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # You can use the 'State' class to
    # interact with the 'states' table in your database
    # Example: Create a new state
    new_state = State(name="New State")
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
