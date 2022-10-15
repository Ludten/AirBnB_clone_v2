#!/usr/bin/python3
"""
flask Application
"""

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
