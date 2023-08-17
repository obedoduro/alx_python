#!/usr/bin/env/python3
"""
Fetches https://alu-intranet.hbtn.io/status with a get request 
"""
import requests

# #def fetch_and_display_status():
#     """
#     Fetches from specified url and displsys it
#     """

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)


# if __name__ == "main":
    # fetch_and_display_status()
print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)