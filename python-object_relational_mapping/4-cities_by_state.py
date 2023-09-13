import MySQLdb
import sys


def list_cities(username, password, database_name):
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

        # Execute the SQL query to retrieve cities with their respective states
        cursor.execute(f"SELECT cities.id,"
        f"cities.name, states.name FROM cities JOIN states "
        f"ON cities.state_id = states.id "
        f"ORDER BY cities.id ASC")

        # Fetch all the rows
        cities = cursor.fetchall()

        # Display the results
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username = sys.argv[1]
        password, database_name = sys.argv[2], sys.argv[3]
        list_cities(username, password, database_name)
