from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_bootstrap import Bootstrap

app = Flask(
    __name__,
    template_folder="assets/templates/",
    static_folder="assets/static/"
)
app.config["SECRET_KEY"] = "pôiujhgjklm"


class SearchForm(FlaskForm):
    search = StringField(render_kw={"placeholder": "rechercher l'article ici..."})

@app.route("/")
def index():
    form = SearchForm()
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)