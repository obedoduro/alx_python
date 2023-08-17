#!/usr/bin/env/python3

import requests
import sys

"""
print(__import__("my_module").__doc__)
"""
def  takes_a_url_and_display(url):


    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    return request_id
    
# print("Body response:")
# print("\t- type:", type(response.text))
# print("\t- content:", response.text)

if  __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    request_id = fetch_request_id(url)
    if request_id:
        print(request_id)
    else:
        print("X-Request-Id header not found in the response.")