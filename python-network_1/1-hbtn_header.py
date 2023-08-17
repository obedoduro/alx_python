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
    takes_a_url_and_display()