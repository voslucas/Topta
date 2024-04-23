# analysing a single word / word part - lemma based - on the lemmas in the txt files
import os
import seaborn as sns
import pandas as pd


# get a list of all txt files that start with #
def get_txt_files():
    txt_files = []
    for file in os.listdir('.'):
        if file.endswith('.txt') and file.startswith('#'):
            txt_files.append(file)
    return txt_files

# read the txt file and get all the lemmas
def get_lemmas(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as f:
        lemmas = f.read().splitlines()
        return lemmas

# get episode number out of the filename, which has structure #<number>.mp3.txt
def get_episode_number(txt_file):
    split_title = txt_file.split(".")
    episode_number = split_title[0].strip("#") 
    #convert to number
    episode_number = int(episode_number)
    return episode_number

# get all 'startswith' lemmas from the txt files
def get_wordpart_lemmas(wordpart):
    files = get_txt_files()
    wordpart_lemmas = set()
    for file in files:
        lemmas = get_lemmas(file)
        for lemma in lemmas:
            if lemma.startswith(wordpart):
                wordpart_lemmas.add(lemma)
    return wordpart_lemmas

variants = get_wordpart_lemmas("aug")
print(variants)

# manual remove augustus and augementeren from the set
variants.remove("augustus")
variants.remove("augmenteren")

counts_per_episode = {}

txt_files = get_txt_files()
for file in txt_files:
    lemmas = get_lemmas(file)
    count =0
    episode = get_episode_number(file)
    # check if one of the variants is in the lemmas
    for lemma in lemmas:
        if lemma in variants:
            count +=1
    counts_per_episode[episode] = count

print(counts_per_episode)


counts_per_episode_df = pd.DataFrame([{"episode": episode, "count": count} for episode, count in counts_per_episode.items()])
# display the counts_per_episode on a seaborn plot with episode on the x-axis and the count on the y-axis using ONLY seaborn


p = sns.relplot(counts_per_episode_df, x='episode', y='count')

p.savefig("aug.png")

