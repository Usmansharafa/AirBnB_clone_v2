#!/usr/bin/python3
"""A module that contains flask routing definitions of a website"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Function that describes the routing of the homepage"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function that describes routing of /HBNB"""
    return 'HBNB'


if __name__ == "__main__":
    app.run('0.0.0.0')
