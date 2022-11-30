#!/usr/bin/python3
"""aaaa"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """aaaa"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """aaaa"""
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text=None):
    """aaaa"""
    return "C " + str(text).replace("_", " ")


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is cool"):
    """aaaa"""
    return "Python " + str(text).replace("_", " ")


@app.route('/number/<n>', strict_slashes=False)
def is_this_a_number(n=0):
    if int(n):
        return n + " is a number"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5000)