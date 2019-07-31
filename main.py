# -*- coding: utf-8 -*-

# ==== IMPORTS SECTION ========================================================
from flask import Flask

# ==== CONSTANTS DEFINITIONS ==================================================

# ==== CLASS DEFINITION =======================================================

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


app.run(host="0.0.0.0")
