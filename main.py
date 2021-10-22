from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_bootstrap import Bootstrap

app = Flask(
    __name__,
    template_folder="assets/templates/",
    static_folder="assets/static/"
)
app.config["SECRET_KEY"] = "pôiujhgjklm"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///assets/search.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
admin = Admin(app, name="Gestion", template_mode="bootstrap4")
bootstrap = Bootstrap(app)


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)

    def __str__(self):
        return self.title

class ArticleAdminView(ModelView):
    pass

class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article

articles_schema = ArticleSchema(many=True)
article_schema = ArticleSchema()


class SearchForm(FlaskForm):
    search = StringField(label="", render_kw={"placeholder": "rechercher l'article ici..."})


@app.route("/api/articles/all/")
def articles_api():
    articles = db.session.query(Article).all()
    return articles_schema.dumps(articles), 200


@app.route("/api/article/<int:article_id>/")
def article_api_detail(article_id):
    article = db.session.query(Article).get(article_id)
    return articles_schema.dumps(article), 200

@app.route("/")
def index():
    form = SearchForm()
    return render_template("index.html", form=form)

@app.route("/article/<int:article_id>/")
def detail(article_id):
    article = db.session.query(Article).get(article_id)
    return render_template("detail.html", article=article)


if __name__ == "__main__":
    db.create_all()
    admin.add_view(ArticleAdminView(Article, db.session))
    app.run(debug=True)