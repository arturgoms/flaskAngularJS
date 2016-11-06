from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for


import os


INI = [True, "0.0.0.0", 8080]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
