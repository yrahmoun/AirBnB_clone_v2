#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displays states """
    state_list = storage.all(State).values()
    sortes = sorted(state_list, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """c loses the storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
