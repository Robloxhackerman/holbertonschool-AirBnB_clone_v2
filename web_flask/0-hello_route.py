#!/usr/bin/python3
"""aaaa"""
from flask import Flask

app = Flask(__name__)
#piporipopaporepo

@app.route('/', strict_slashes=False)
def holinga():
    """aaaa"""
    return("Hello HBNB!")
#aaaaaaaaaaaaaa
if __name__ == '__main__':
    app.run(host="0.0.0.0")