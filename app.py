from flask import Flask
from db import get_geometry_json, get_event_json

app = Flask(__name__)

@app.route('/')
def dummy():
    """ For testing - always return fixed JSON from base URL """
    with open("examples/geometry_run_7-2076.json") as f:
        return "\n".join(f.readlines())


@app.route('/geometry/<period_number>/<run_number>')
def geometry(period_number, run_number):
    """ Actually get geometry from ROOT and return it to client """
    return get_geometry_json(period_number, run_number)


@app.route('/event/<event_idx>')
def event(event_idx):
    """ Get event number event_idx from a given file """
    return get_event_json(event_idx)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50000, debug=True)

