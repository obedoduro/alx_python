"""
This is a sample module to run on
host 0.0.0
port 5000
"""
from flask import Flask

# Create a Flask web application
app = Flask(__name__)


# Define a route for the root path with strict_slashes=False
"""
This module helps route in the function hello_HBNB

"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route: /
    Displays "Hello HBNB!"

    Returns:
        str: A greeting message.
    """
    return "Hello HBNB!"

# Define a route for /hbnb with strict_slashes=False
"""
This module helps route in the function HBNB

"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route: /hbnb
    Displays "HBNB"

    Returns:
        str: A message.
    """
    return "HBNB"

# Run the application on 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
