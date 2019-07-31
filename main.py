# -*- coding: utf-8 -*-

# ==== IMPORTS SECTION ========================================================
import flask

# ==== CONSTANTS DEFINITIONS ==================================================

# ==== CLASS DEFINITION =======================================================

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run()
