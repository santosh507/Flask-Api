from flask import jsonify
from wsgi import app_logger


def test_api():
    app_logger.debug("Testing testApi endpoint View")
    app_logger.info("In testApi endpoint View")
    return jsonify({"Message": "Hello World"})


def test_api_clone():
    app_logger.debug("Testing testApiClone endpoint View")
    app_logger.info("In testApiClone endpoint View")
    return jsonify({"Message": "Hello World"})
