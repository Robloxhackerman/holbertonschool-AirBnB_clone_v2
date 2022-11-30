#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

from flask import Flask

app = Flask(__name__)
"""aaaa"""

@app.route('/', strict_slashes=False)
def holinga():
    """aaaa"""
    return("Hello HBNB!")

app.run(host="0.0.0.0")