#!/usr/bin/python3
"""aaaa"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def holinga():
    """aaaa"""
    return("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """aaaa"""
    return("HBNB")


@app.route('/c/<text>', )
def c(text=None):
    """aaaa"""
    return "C " + str(text).replace("_", " ")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
