#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_route():
    """Display the states in order”"""
    states = storage.all('State').values()
    t_name = 'State'
    return render_template('7-states_list.html', states=states, t_name=t_name)


@app.teardown_appcontext
def teardown(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
