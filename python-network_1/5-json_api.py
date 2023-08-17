import requests
import sys

def search_user_with_letter(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the provided letter as a parameter.
    
    Args:
        letter (str): The letter to search for.
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": letter}

    try:
        response = requests.post(url, data=payload)
        json_data = response.json()

        if json_data:
            user_id = json_data.get("id", "")
            user_name = json_data.get("name", "")
            if user_id and user_name:
                print(f"[{user_id}] {user_name}")
            else:
                print("No result")
        else:
            print("No result")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        search_user_with_letter("")
    else:
        letter = sys.argv[1]
        search_user_with_letter(letter)
