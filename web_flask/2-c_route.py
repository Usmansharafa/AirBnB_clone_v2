#!/usr/bin/python3
"""A module that contains flask routing definitions of a website"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Function that describes the routing of the homepage"""
    return 'Hello HBNB!\n'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function that describes routing of /HBNB"""
    return 'HBNB\n'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Function that describes routing of /c/<text>"""
    new_text = " ".join(text.split('_'))
    return f'C {new_text}\n'


if __name__ == "__main__":
    app.run('0.0.0.0')
