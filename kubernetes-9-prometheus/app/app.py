import os
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from marshmallow import ValidationError
from prometheus_client import generate_latest
from metrics import register_metrics


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URI"]


db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
register_metrics(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60))
    username = db.Column(db.String(60))
    firstName = db.Column(db.String(60))
    lastName = db.Column(db.String(60))
    phone = db.Column(db.String(60))


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route("/health")
def health():
    return '{"status": "ok"}'


@app.route("/")
def hello():
    greeting = os.environ.get('GREETING', 'Hello')
    return greeting + " from " + os.environ["HOSTNAME"] + " !"


def get_user(id):
    user = User.query.get(id)
    if user is None:
        abort(404)
    return user


@app.errorhandler(ValidationError)
def handle_invalid(error):
    response = jsonify(error.messages)
    response.status_code = 402
    return response


@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)


@app.route("/users", methods=["Post"])
def create_user():
    user = user_schema.load(request.json)
    db.session.add(user)
    db.session.commit()

    return user_schema.jsonify(user)


@app.route("/users/<id>")
def user_detail(id):
    user = get_user(id)
    return user_schema.jsonify(user)


@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    user = get_user(id)
    user = user_schema.load(request.json, instance=user)
    db.session.commit()
    return user_schema.jsonify(user)


@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    user = get_user(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)


@app.route('/metrics')
def metrics():
    return generate_latest()

@app.route('/error')
def error():
    from flask import Response
    return Response("eror", status=501, mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
