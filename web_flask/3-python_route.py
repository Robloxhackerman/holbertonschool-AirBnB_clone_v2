#!/usr/bin/python3
"""aaaa"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def holinga():
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
def c(text="is cool"):
    """aaaa"""
    return "Python " + str(text).replace("_", " ")


if __name__ == "main":
    """aaaaaaaaaa"""
    app.run(host="0.0.0.0")
