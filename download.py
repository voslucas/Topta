import os
import codecs
import json
import urllib.request


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

# download the episode
def download_episode(episode):
    url = episode['audio_url']
    title = episode['title']
    episode_number = get_episode_number(title)
    filename = episode_number + ".mp3"
    print("Downloading", filename)
    urllib.request.urlretrieve(url, filename)
    print("Downloaded", filename)

# download all the episodes in the data.json file if they are not already downloaded
def download_all_episodes():
    episodes = get_episodes()
    for episode in episodes:
        title = episode['title']
        episode_number = get_episode_number(title)
        filename = episode_number + ".mp3"
        if not os.path.exists(filename):
            download_episode(episode)
        else:
            print("Already downloaded", filename)
    print("All episodes downloaded")


download_all_episodes()