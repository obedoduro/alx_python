#!/urs/bin/env/python3

import requests
import sys

"""
errorcode takes Url , send request to Url and display the body
"""
def errorcode(url):
    """
    Fetches the content of a URL and displays the response body.
    
    If the HTTP status code is greater than or equal to 400, an error message
    is printed along with the error code.
    
    Args:
        url (str): The URL to send a request to.
    """

    try:
        response = requests.get(url)
        print("Response Body: ")
        print(repsonse.text)

        if reponse.status_code >= 400:
            print(f"Error code: {response.status_code}")
        
        # if response.status_code < 400:
        #     print("Regular request")


    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)  


if __name__ == "__main__":
    if len(sys.argv)  != 3:
        print("Regular request".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response_body = errorcode(url)
    print(response_body)
