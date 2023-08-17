import requests
import sys
import os

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
    github_username = os.environ.get("GITHUB_USERNAME")
    github_token = os.environ.get("GITHUB_TOKEN")
    
    if github_username and github_token:
        get_github_id(github_username, github_token)
    else:
        print("Please set GITHUB_USERNAME and GITHUB_TOKEN environment variables.")
