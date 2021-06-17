import urllib.request
import ssl
from behave import given, when, then


@given("Getting respond from Google")
def respond(context):
    url = urllib.request.urlopen("http://www.google.com/")
    print("result Code: " + str(url.getcode()))
    if (url.getcode() == 200):
        data = url.read()
        print(data)
    else:
        print("Received Error")






