#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, abort, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display “HBNB”"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_is_fun(text):
    """Display “C ” followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def p_is_fun(text='is cool'):
    """Display “Python ” followed by the value of the text variable """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display “n is a number” only if n is an integer """
    return '{} is a number'.format(n) if int(n) else abort(404)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display “n is a number” only if n is an integer """
    return render_template('5-number.html', n=n) if int(n) else abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
