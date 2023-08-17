#!/usr/bin/env/python3

import requests
import sys

"""
print(__import__("my_module").__doc__)
"""
def  takes_a_url_and_display(url):
    """
    Sends a request to the given URL with the X-Request-Id header and displays the response.
    """
    headers = {'X-Request-Id': 'School'}
    response = requests.get(url, headers=headers)
    return response.text
    
# print("Body response:")
# print("\t- type:", type(response.text))
# print("\t- content:", response.text)

if  __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    response = fetch_response(url)
    print(response)