from flask import Flask
import requests
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/raw")
def raw():
    url = 'https://api.github.com/orgs/CiscoDevNet/repos'
    return render_template('show-raw.html', data=requests.get(url).json())

@app.route("/results")
def results():
    url = 'https://api.github.com/orgs/CiscoDevNet/repos'
    print(requests.get(url).json())
    return render_template('show-results.html', data=requests.get(url).json())





if __name__ == '__main__':
    app.run(debug=True)