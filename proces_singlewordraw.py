# analysing a single word / word part on the raw json text
import os
import json
import seaborn as sns
import pandas as pd


base_dir = './data'

# get a list of all txt files that start with #
def get_json_files():
    txt_files = []
    for file in os.listdir(base_dir):
        if file.endswith('.json') and file.startswith('#'):
            txt_files.append(file)
    return txt_files

# read the txt file and get all the lemmas
def extract_text_from_json(json_file):
    filename = os.path.join(base_dir, json_file)
    with open(filename, 'r') as f:
        data = json.load(f)
        text = data['combinedRecognizedPhrases'][0]['display']
        # remove all punctuation
        text = text.replace(".", "")
        text = text.replace(",", "")
        text = text.replace("!", "")
        text = text.replace("?", "")
        text = text.replace(":", "")
        text = text.replace(";", "")
        text = text.replace("(", "")
        text = text.replace(")", "")
        text = text.replace("[", "")
        text = text.replace("]", "")
        text = text.replace("{", "")
        text = text.replace("}", "")

        text = text.lower()
        return text




# get episode number out of the filename, which has structure #<number>.mp3.txt
def get_episode_number(txt_file):
    split_title = txt_file.split(".")
    episode_number = split_title[0].strip("#") 
    #convert to number
    episode_number = int(episode_number)
    return episode_number

# get all 'startswith' words from the txt files
def get_wordparts(wordpart):
    files = get_json_files()
    wordparts = set()
    for file in files:
        doc = extract_text_from_json(file)
        words = doc.split(" ")
        for word in words:
            if word.startswith(wordpart):
                wordparts.add(word)
    return wordparts

variants = get_wordparts("aug")
print(variants)

# manual remove augustus and augementerend from the set
variants.remove("augustus")
variants.remove("augmenterend")

#variants.remove('fascist')
#variants.remove('fasciscus')
#variants.remove('fascisme')
#variants.remove('fascistische')
#variants.remove('fascisten')
#variants.remove('fascistisch')


counts_per_episode = {}

jsonfiles = get_json_files()
for file in jsonfiles:
    doc = extract_text_from_json(file)
    words = doc.split(" ")
    count =0
    episode = get_episode_number(file)
    # check if one of the variants is in the lemmas
    for word in words:
        if word in variants:
            count +=1
    counts_per_episode[episode] = count

print(counts_per_episode)

# count the number of episode which have 0 counts
zero_counts = 0
for episode, count in counts_per_episode.items():
    if count == 0:
        zero_counts +=1

print('number of episodes with NO Augustinus',zero_counts)

counts_per_episode_df = pd.DataFrame([{"episode": episode, "count": count} for episode, count in counts_per_episode.items()])
# display the counts_per_episode on a seaborn plot with episode on the x-axis and the count on the y-axis using ONLY seaborn

sns.set_theme()

p = sns.relplot(counts_per_episode_df, x='episode', y='count')

p.savefig("aug-raw.png")

