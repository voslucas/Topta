# Extract all descriptions for each episode from the data.json file and save it to a text file
# It is used to extract the guests per episode (see README) with ChatGPT.

import os
import codecs
import json

# read the data.json file and get all the episodes
def get_episodes():
    with codecs.open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        episodes = data['episodes']
        return episodes
    
# a title consist of the episodenumer and the title of the episode
# we split the title and return the episode number based on the - separator
# and truncate the title
def get_episode_number(title):
    split_title = title.split("-")
    episode_number = split_title[0].strip()
    return episode_number


with open('descriptions.txt', 'w', encoding='utf-8') as f:
    episodes = get_episodes()
    for episode in episodes:
        number = get_episode_number(episode["title"])
        desc = episode["description"]
        print(number, file=f)
        print(desc, file=f)

