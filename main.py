import os

from flask import Flask, render_template, request, jsonify, abort
from core import db
from model.names import Name


def create_app():
    new_app = Flask(__name__)
    new_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URL']
    new_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    new_app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    db.init_app(new_app)
    with new_app.app_context():
        db.create_all()
        return new_app


app = create_app()


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/say_hello", methods=["POST"])
def say_hello():
    sent_name = request.get_json()["name"]
    name_in_db = Name.get_name(sent_name)

    if name_in_db is None:
        Name.create(name=sent_name)
        return jsonify({"result": "Привіт, " + sent_name}, 200)

    return jsonify({"result": "Вже бачилися, " + sent_name}, 200)


@app.route("/all_names/<page>")
def all_names(page):
    page_size = 10
    page = int(page)
    if page < 1:
        abort(404)
    names_count = Name.names_count()
    pages = (names_count // page_size) + (1 if names_count % 10 > 0 else 0)
    if page > pages:
        abort(404)
    names = Name.get_all_names(page, page_size)
    return render_template("all_names.html", names=names, page=page, pages=pages)


if __name__ == "__main__":
    app.run(debug=True)
