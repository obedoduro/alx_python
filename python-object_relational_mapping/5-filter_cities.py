import MySQLdb
import sys


def list_cities_by_state(username, password, database_name, state_name):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            user=username,
            passwd=password,
            host='localhost',
            port=3306,
            db=database_name
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Create the SQL query with placeholders and pass user input as a tuple
        query = ("SELECT cities.name FROM cities JOIN states ON "
                 "cities.state_id = states.id WHERE states.name = %s "
                 "ORDER BY cities.id ASC")
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        cities = cursor.fetchall()

        # Extract city names and join them into a comma-separated string
        city_names = ', '.join(city[0] for city in cities)

        # Display the comma-separated city names
        print(city_names)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username>"
              " <password> <database_name> <state_name>")
    else:
        username, password = sys.argv[1], sys.argv[2]
        database_name, state_name = sys.argv[3], sys.argv[4]
        list_cities_by_state(username, password, database_name, state_name)
