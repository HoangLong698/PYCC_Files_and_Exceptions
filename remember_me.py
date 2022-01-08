import json

# Load the username, if it has been stored previously
# otherwise, prompt for the username and store it

def get_stored_username():
    # Get stored username if available.
    filename = 'username.json'
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    # Prompt for a new username and storing it.
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    # Great the user by name.
    username = get_stored_username()
    prompt = input(f"Your name is {username} right? [Y|y] or [N|n]: ")
    if prompt.lower() == "y":
            print(f"Welcome back, {username}")   
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back. {username}")

greet_user()
