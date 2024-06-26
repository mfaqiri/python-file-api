from flask import Flask, redirect, send_from_directory, url_for,abort
import json
import os
import re

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/<file>", methods=["GET"])
def file_api(file):

    print(file)
    pattern = re.compile(r'[A-Za-z]+')

    if pattern.fullmatch(file):

        with open(os.path.join(app.root_path, "endpoints/"+file+".json"), "r") as data:
            data = json.load(data)
            return data
    else:
        abort(404, 'invalid endpoint name')
