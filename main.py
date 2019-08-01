# -*- coding: utf-8 -*-

# ==== IMPORTS SECTION ========================================================
import flask

# ==== CONSTANTS DEFINITIONS ==================================================

# ==== CLASS DEFINITION =======================================================

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return flask.send_from_directory('.', 'index.html')


app.run(host="0.0.0.0")
