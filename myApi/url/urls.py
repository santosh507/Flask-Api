from myApi.url import myApi
from myApi.implementation.api_test import test_api

myApi.add_url_rule('/TestApi',"test api",test_api,methods=['GET'])