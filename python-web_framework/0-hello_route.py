"""
This is a sample module to run on
host 0.0.0
port 5000
"""
from flask import Flask

app = Flask(__name__)

"""
This module helps route in the function hello_HBNB

"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
