import requests
import sys

def get_github_id(username, token):
    """
    Fetches the GitHub user ID using Basic Authentication with a personal access token.
    
    Args:
        username (str): Your GitHub username.
        token (str): Your GitHub personal access token.
    """
    api_url = "https://api.github.com/user"
    auth = (username, token)
    
    try:
        response = requests.get(api_url, auth=auth)
        
        if response.status_code == 200:
            response_json = response.json()
            if "id" in response_json:
                print(response_json["id"])
            else:
                print("Unable to retrieve GitHub ID.")
        elif response.status_code == 401:
            print("None")
        else:
            print(f"An error occurred. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    github_username = sys.argv[1]
    github_token = sys.argv[2]
    get_github_id(github_username, github_token)