from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    with open("geometry_run_7-2076.json") as f:
        return "\n".join(f.readlines())


