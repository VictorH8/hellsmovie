from flask import Flask
import requests
import json

from routes import *

app = Flask(__name__)

app.route('/', methods=['GET', 'POST'])(home)
app.route('/search',methods=['GET','POST'])(search)

if __name__ == "__main__":
    app.run(debug=True)
