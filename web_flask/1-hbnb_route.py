#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def holinga():
    """aaaa"""
    return("Hello HBNB")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """aaaa"""
    return("HBNB")

app.run(host="0.0.0.0")