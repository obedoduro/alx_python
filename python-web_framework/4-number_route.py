"""
This is a sample module to run on
host 0.0.0
port 5000
"""
from flask import Flask, escape

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root path with strict_slashes=False
"""
This module helps route in the function HBNB

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

# Define a route for /c/<text> with strict_slashes=False
"""
This module helps route in the function c_text

"""
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route: /c/<text>
    Displays "C " followed by the value of the text variable.
    Replace underscore (_) symbols with a space.

    Args:
        text (str): The text to display.

    Returns:
        str: The formatted message.
    """
    formatted_text = escape(text).replace('_', ' ')
    return "C " + formatted_text

# Define a route for /python/<text> with strict_slashes=False
"""
This module helps route in the function pythontext

"""
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route: /python/<text>
    Displays "Python " followed by the value of the text variable.
    Replace underscore (_) symbols with a space.

    Args:
        text (str): The text to display.

    Returns:
        str: The formatted message.
    """
    formatted_text = escape(text).replace('_', ' ')
    return "Python " + formatted_text

# Define a route for /number/<n> with strict_slashes=False
"""
This module helps route in the function is_number

"""
@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Route: /number/<n>
    Displays "n is a number" if n is an integer.

    Args:
        n (int): The number to check.

    Returns:
        str: The result message.
    """
    if isinstance(n, int):
        return f"{n} is a number"
    else:
        return "Not a number"

# Run the application on 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
