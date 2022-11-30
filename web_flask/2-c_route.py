#!/usr/bin/python3
"""aaaa"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def holinga():
    return("Hello HBNB!")

@app.route('/HBNB')
def hbnb():
    return("HBNB")

@app.route('/c/<text>', )
def method_name():
    pass

app.run(host="0.0.0.0")