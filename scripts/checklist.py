import json
import requests

api_key = input("API key??")
api_token = input("API token??")
board_id = input("Board id??")
url = "https://api.trello.com/1/boards/" + board_id + "/checklists" + "?fields=idChecklists&key=" + api_key + "&token=" + api_token

response = json.loads(requests.request("GET", url).text)
checklistIds = [item["name"] for checkItem in response for item in checkItem["checkItems"] if item["state"] == "incomplete"]
print(checklistIds)
