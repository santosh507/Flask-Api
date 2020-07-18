from wsgi.myApi.url import myApi
from wsgi.myApi.implementation.api_test import test_api, test_api_clone

myApi.add_url_rule('/testApi', "test api", test_api, methods=['GET'])
myApi.add_url_rule('/testApiClone', "test api clone", test_api_clone, methods=['GET'])
