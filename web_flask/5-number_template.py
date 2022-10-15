#!/usr/bin/python3
"""
flask Application
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    A function for routing requests passed to
    '/'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    A function for routing requests passed to
    '/hbnb'
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    A function for routing requests passed to
    '/c/<text>'

    Returns:
        C <text>
    """
    if ('_' in text):
        text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', defaults={'text': None}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_cool(text):
    """
    A function for routing requests passed to
    '/hbnb'

    '/python/<text>'

    Returns:
        Python <text> or Python is cool
    """
    if (text is None):
        text = 'is cool'
    if ('_' in text):
        text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    A function for routing requests passed to
    '/number/<n>' and checks if n is an integer

    Returns:
        n or None
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """
    A function for routing requests passed to
    '/number_template/<n>' and checks if n is an integer

    Returns:
        html template of number or None
    """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
