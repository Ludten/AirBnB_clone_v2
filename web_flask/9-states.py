#!/usr/bin/python3
"""
flask Application
"""

from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    from models.state import State
    """
    A function for routing requests passed to
    '/states'
    """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', storage=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    from models.state import State
    """
    A function for routing requests passed to
    '/states/<id>'
    """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template('9-states.html', storage=states, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
