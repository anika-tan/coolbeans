# get quote

import requests
import json

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    line = json_data[0]["q"] + "\n" + "- " + json_data[0]["a"] # get quote and author
    return line