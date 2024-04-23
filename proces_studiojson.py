# The Azure Speech Studio / API / CLA generates json files as a result, which needed processing to extract the json/text files

# open the studio1.json file 
# for each record in values get the name and links, in the links is a contentUrl
# download the contentUrl and save it as mp3 file

import json
import requests
import os

def download_json_files():
    with open('studio4.json', 'r') as f:
        data = json.load(f)
        for record in data['values']:

            # the name is formatted as "input/#1.mp3.json"
            # skip the input/ part 
            name = record['name']
            name = name.split('/')[1]

            links = record['links']
            contentUrl = links['contentUrl']
            r = requests.get(contentUrl)
            with open(name, 'wb') as f:
                f.write(r.content)


download_json_files()