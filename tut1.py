from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

@app.route("/")
def hello():

    return render_template('index.html')

@app.route("/about")
def harry():
    name = "Bhupender Gamer "
    return render_template('about.html', name2= name)

@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')

app.run(debug=True)