from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)