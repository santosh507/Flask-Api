from flask import jsonify


def test_api():
    return jsonify({"Message": "Hello World"})


def test_api_clone():
    return jsonify({"Message": "Hello World"})
