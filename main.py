import os

from flask import Flask, render_template, request, jsonify
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


if __name__ == "__main__":
    app.run(debug=True)
