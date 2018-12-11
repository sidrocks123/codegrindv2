from flask import Flask, redirect, url_for, request, render_template

from string import Template
import subprocess
import re
import base64

app = Flask(__name__)
#date='241095'

@app.route('/')
def homepage():
    return render_template("Hotel-Domestic(IN).html")

@app.route('/airfare')
def airfare2():
    return render_template("Airfare-Domestic.html")

@app.route('/car')
def cr():
    return render_template("CarRental(IN).html")






if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
