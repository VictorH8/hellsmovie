from flask import Flask

from routes import *
from utils import *

app = Flask(__name__)

app.route('/', methods=['GET', 'POST'])(home)
app.route('/search',methods=['GET','POST'])(search)
app.route('/<string:nome>')(erro)

if __name__ == "__main__":
    app.run(debug=True)
