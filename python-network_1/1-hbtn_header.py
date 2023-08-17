#!/usr/bin/env python3
"""
Sends a request to a URL then displays the value of the X-Request-Id header in the response.
"""

import requests
import sys

def fetch_request_id(url):
    """
    Fetches the value of the X-Request-Id header from the response of the given URL.
    """
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    return request_id

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    request_id = fetch_request_id(url)
    if request_id:
        print(request_id)
    else:
        pass