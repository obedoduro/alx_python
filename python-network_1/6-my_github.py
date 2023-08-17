#!/usr/bin/env/python3
import sys
import requests


def get_github_id(username, token):
    """
    Fetches the GitHub user ID using Basic Authentication with a personal access token.
    
    Args:
        username (str): Your GitHub username.
        token (str): Your GitHub personal access token.
    """
    api_url = "https://api.github.com/user"
    headers = {
        "Authorization": f"Basic {username}:{token}"
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        response_json = response.json()
        
        if "id" in response_json:
            print(f"Your GitHub ID is: {response_json['id']}")
        else:
            print("Unable to retrieve GitHub ID.")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
    except ValueError:
        print("Response is not valid JSON.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide your GitHub username and personal access token as arguments.")
    else:
        github_username = sys.argv[1]
        github_token = sys.argv[2]
        get_github_id(github_username, github_token)
