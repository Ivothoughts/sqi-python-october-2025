import requests

url = "https://jsonplaceholder.typicode.com/users"

responses = requests.get(url).json()

def fetch_user_data():
    user_store_holder = []
    for user in responses:
        if "username" in user:
            user_store_holder.append(user["username"])
    return user_store_holder


