from flask import jsonify

def test_api():
    return jsonify({"Message":"Hello World"})