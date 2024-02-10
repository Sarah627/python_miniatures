import json
import requests
from sys import argv, exit

if len(argv) != 2:
    exit()
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=20&term="+argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
