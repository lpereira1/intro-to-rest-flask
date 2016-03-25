from flask import Flask
import requests
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
from flask import render_template
import json

app = Flask(__name__)

# create the route for the landing page
@app.route('/')
def index():
    return render_template('index.html')


# create the route to retrieve list of repositories and display unformatted json
@app.route("/raw")
def raw():
    # specify the url
    url = 'https://api.github.com/orgs/CiscoDevNet/repos'
    # call the api endpoint using GET method of requests library
    # pass the returned data to the show-raw.html template to display
    return render_template('show-raw.html', data=requests.get(url).json())


# create the route to retrieve list of repositories and display list of repository names
@app.route("/results")
def results():
    # specify the url
    url = 'https://api.github.com/orgs/CiscoDevNet/repos'
    # call the api endpoint using GET method of requests library
    # pass the returned data to the show-results.html template to display
    return render_template('show-results.html', data=requests.get(url).json())





if __name__ == '__main__':
    app.run(debug=True)