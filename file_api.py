from flask import Flask, redirect, send_from_directory, url_for
import json
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/<file>")
def file_api(file):

    with open(os.path.join(app.root_path, "endpoints/"+file+".json"), "r") as data:
        data = json.load(data)
        return data
