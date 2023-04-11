from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.user.views import get_user_name

article = Blueprint("article", __name__, url_prefix="/article", static_folder="../static")

ARTICLES = {
    1: {
        "title": "Title_1",
        "text": "Random_texts",
        "author": 3
    },
    2: {
        "title": "Title_2",
        "text": "Random again",
        "author": 2
    },
    3: {
        "title": "Title_3",
        "text": "Very difficult description",
        "author": 1
    },
    4: {
        "title": "Title_4",
        "text": "Not so difficult description",
        "author": 3
    }
}


@article.route("/")
def article_list():
    return render_template(
        "articles/list.html",
        articles=ARTICLES
    )


@article.route("/<int:pk>")
def get_article(pk: int):
    if pk in ARTICLES:
        article_raw = ARTICLES[pk]
    else:
        raise NotFound("Article id:{}, not found".format(pk))
    title = article_raw["title"]
    text = article_raw["text"]
    author = get_user_name(article_raw["author"])
    return render_template(
        "articles/details.html",
        title=title,
        text=text,
        author=author
    )