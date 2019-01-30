#!/usr/bin/python3
"""
web application to generate list of states dynamically
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True


@app.teardown_appcontext
def close(exception):
    """Closes the database again at the end of the request."""
    storage.close()


@app.route('/states_list')
def states():
    """access File/DB Storage for all State objects and render to HTML"""
    state = storage.all('State')
    return render_template('7-states_list.html', states=state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
