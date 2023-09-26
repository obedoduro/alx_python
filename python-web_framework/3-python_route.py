from flask import Flask, escape

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root path with strict_slashes=False
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
@app.route('/c/<text>', strict_slashes=False)
@app.route('/c/', strict_slashes=False)
def c_text(text="is_cool"):
    """
    Route: /c/<text>
    Displays "C " followed by the value of the text variable.
    Replace underscore (_) symbols with a space.

    Args:
        text (str, optional): The text to display. Defaults to "is_cool".

    Returns:
        str: The formatted message.
    """
    formatted_text = escape(text).replace('_', ' ')
    return "C " + formatted_text

# Define a route for /python/<text> with strict_slashes=False
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text="is_cool"):
    """
    Route: /python/<text>
    Displays "Python " followed by the value of the text variable.
    Replace underscore (_) symbols with a space.

    Args:
        text (str, optional): The text to display. Defaults to "is_cool".

    Returns:
        str: The formatted message.
    """
    formatted_text = escape(text).replace('_', ' ')
    return "Python " + formatted_text

# Run the application on 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
