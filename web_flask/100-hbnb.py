#!/usr/bin/python3
"""script that starts a Flask web application"""
import models
from flask import Flask, abort, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def all_states():
    states = models.storage.all(State).values()
    cities = models.storage.all(City).values()
    amenities = models.storage.all(Amenity).values()
    places = models.storage.all(Place).values()

    return render_template(
                           '100-hbnb.html',
                           states=states,
                           cities=cities,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def teardown(self):
    """remove the current SQLAlchemy Session"""
    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
