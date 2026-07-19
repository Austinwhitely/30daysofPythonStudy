# let's import the flask

from flask import Flask, Response, request, jsonify
import json
import os

app = Flask(__name__)


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {"user_id": user_id, "name": "John Doe", "email": "joh.doe@example.com"}
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
