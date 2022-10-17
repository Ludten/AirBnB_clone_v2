#!/usr/bin/python3
"""
flask Application
"""

from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    from models.state import State
    from models.amenity import Amenity
    from models.place import Place
    from models.user import User
    """
    A function for routing requests passed to
    '/hbnb'
    """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    amenities = list(storage.all(Amenity).values())
    places = list(storage.all(Place).values())
    users = list(storage.all(User).values())
    return render_template('10-hbnb_filters.html', storage=states,
                           amenities=amenities, places=places,
                           users=users)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
