#!/usr/bin/python3
"""
web application to generate list of states dynamically
"""
from flask import Flask
from models import storage
app = Flask(__name__)


@app.route
def states
states = storage.all()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
