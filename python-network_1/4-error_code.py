#!/urs/bin/env/python3

import requests
import sys

"""
errorcode takes Url , send request to Url and display the body
"""
def errorcode():
    req = urllib.request.Request('http://www.python.org/fish.html')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())  


if __name__ == "__main__":
    errorcode()


