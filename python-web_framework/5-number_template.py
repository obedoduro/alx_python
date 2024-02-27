"""
This script creates a Flask web application with various routes.

Routes:
- /: Displays "Hello HBNB!"
- /hbnb: Displays "HBNB"
- /c/<text>: Displays "C " followed by the value of the text variable (underscores replaced with spaces)
- /python/<text>: Displays "Python " followed by the value of the text variable (underscores replaced with spaces)
- /number/<n>: Displays "n is a number" only if n is an integer
- /number_template/<n>: Displays an HTML page only if n is an integer:
    - H1 tag: "Number: n" inside the tag BODY

The option strict_slashes=False is used in route definitions to handle both /endpoint and /endpoint/ URLs.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route: /
    Displays "Hello HBNB!"
    
    Returns:
        str: A greeting message.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route: /hbnb
    Displays "HBNB"
    
    Returns:
        str: A message.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route: /c/<text>
    Displays "C " followed by the value of the text variable.
    Replace underscore (_) symbols with a space.

    Args:
        text (str): The text to display.

    Returns:
        str: The formatted message.
    """
    formatted_text = text.replace('_', ' ')
    return "C " + formatted_text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route: /python/<text>
    Displays "Python " followed by the value of the text variable.
    Replace underscore (_) symbols with a space.

    Args:
        text (str): The text to display.

    Returns:
        str: The formatted message.
    """
    formatted_text = text.replace('_', ' ')
    return "Python " + formatted_text


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Route: /number/<n>
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Route: /number_template/<n>
    Displays an HTML page only if n is an integer:
    - H1 tag: "Number: n" inside the tag BODY

    Args:
        n (int): The number to display.

    Returns:
        str: The HTML page.
    """
    if isinstance(n, int):
        return render_template('5-number.html', number=n)
    else:
        return "Not a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
