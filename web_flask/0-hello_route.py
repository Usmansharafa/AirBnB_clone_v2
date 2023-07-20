#!/usr/bin/python3
"""A module that contains a flask routing for homepage of a website"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Function that describes the routing of the homepage"""
    return 'Hello HBNB!\n'


if __name__ == "__main__":
    app.run('0.0.0.0')
