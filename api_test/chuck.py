import requests
import pprint as p

URL = "https://api.chucknorris.io/jokes/random"


def get_joke():
    response = requests.get(URL)
    status = response.status_code
    return f"{response.json()['value']}, {response.json()['created_at']}. STATUS CODE : {status}"


p.pprint(get_joke())
