#!/usr/bin/python3
"""A module that contains flask routing definitions of a website"""


from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Function that describes the routing of the homepage"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function that describes routing of /HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Function that describes routing of /c/<text>"""
    new_text = " ".join(text.split('_'))
    return f'C {new_text}'


@app.route('/python')
@app.route('/python/<text>/', strict_slashes=False)
def python_text(text='is_cool'):
    """Function that describes routing of /python/<text>"""
    new_text = " ".join(text.split('_'))
    return f'Python {new_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Function that describes routing of /number/<n>"""
    if isinstance(n, int):
        return f'{n} is a number'
    abort(404)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    abort(404)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even_route(n):
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)
    abort(404)


if __name__ == "__main__":
    app.run('0.0.0.0')
