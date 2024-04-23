import os
import json
from tqdm import tqdm

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


file_lemmas = {}
global_lemmas = set()
files = get_txt_files()
for file in files:
    lemmas = get_lemmas(file)
    file_lemmas[file] = get_lemmas(file)
    global_lemmas.update(lemmas)

# go through all the global_lemma's.
# for each global lemma , count the number of files that contain the lemma as well
# store the result in a dictionary
global_lemma_count = {}
for lemma in tqdm(global_lemmas):
    count = 0
    for file in file_lemmas:
        if lemma in file_lemmas[file]:
            count += 1
    global_lemma_count[lemma] = count

# sort the global_lemma_count dictionary based on the count descending
sorted_global_lemma_count = dict(sorted(global_lemma_count.items(), key=lambda item: item[1], reverse=True))

# display the top 100 lemma's
for i, (lemma, count) in enumerate(sorted_global_lemma_count.items()):
    print(i, lemma, count)
    if i == 99:
        break

