#!/usr/bin/python3
from flask import Flask, escape
"""Accept only a integer"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Return a str"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """Return a str"""
    return 'HBNB'


@app.route('/c/<text>')
def TEXT(text):
    """Return a str"""
    text = str(text).replace("_", " ")
    return 'C {}'.format(escape(text))


@app.route('/python/<text>')
@app.route('/python')
@app.route('/python/')
def is_cool(text='is cool'):
    """Return a str with differents routes"""
    text = str(text).replace("_", " ")
    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>')
def integer(n):
    """Display only if n is an integer"""
    return '{} is a number'.format(escape(n))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
