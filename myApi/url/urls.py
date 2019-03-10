from myApi.url import myApi
from myApi.implementation.api_test import test_api,test_api_1

myApi.add_url_rule('/testApi',"test api",test_api,methods=['GET'])
myApi.add_url_rule('/testApi1',"test api 1",test_api_1,methods=['GET'])