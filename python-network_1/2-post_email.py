#!/usr/bin/env/python3
"""
Sends a POST request to a URL with an email an display the response body
"""

import requests
import sys

def take_url_and_email(url, email):
    """
    Sends a post request to the given URL with the email
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)
    return response.text

if __name__ == "__main__":
    if len(sys.argv)  != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response_body = take_url_and_email(url, email)
    print(response_body)