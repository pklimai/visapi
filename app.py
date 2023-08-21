from flask import Flask

app = Flask(__name__)

from db import get_geometry_json

@app.route('/')
def dummy():
    """ For testing - always return fixed JSON from base URL """
    with open("examples/geometry_run_7-2076.json") as f:
        return "\n".join(f.readlines())

@app.route('/geometry/<period_number>/<run_number>')
def geometry(period_number, run_number):
    """ Actually get geometry from ROOT and return it to client """
    return get_geometry_json(period_number, run_number)

