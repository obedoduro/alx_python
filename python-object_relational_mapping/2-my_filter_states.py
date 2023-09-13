import MySQLdb
import sys

def search_states(username, password, database_name, state_name):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            user=username,
            passwd=password,
            host='localhost',
            port=3306,
            db=database_name,
            charset='utf8'
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Create the SQL query with a parameterized query
        query = "SELECT * FROM states WHERE name = %s"
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        search_states(username, password, database_name, state_name)
    else:
        print("Usage: python script.py <username> <password> <database_name> <state_name>")
