import os
import json
import spacy

# our json file of each episode needs some cleaning
# we use channel 0 of the text in the json file, 
# skip the punctuation and make it lowercase
# find the lemma's of each words in the text
# store the lemma's in a new txt file next to the json file

nlp = spacy.load('nl_core_news_sm')


# find all the json files of the structure #<number>.mp3.json
def get_json_files():
    json_files = []
    for file in os.listdir('.'):
        if file.endswith('.json') and file.startswith('#'):
            json_files.append(file)
    return json_files


def extract_text_from_json(json_file):
    with open(json_file, 'r') as f:
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
    

files = get_json_files()
for file in files:
    text = extract_text_from_json(file)
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc if not token.is_stop]
    lemmas = set(lemmas)
    # order the lemmas
    lemmas = sorted(lemmas)
    with open(file.replace(".json", ".txt"), "w", encoding='utf-8') as f:
        f.write("\n".join(lemmas))
        print("Written", file.replace(".json", ".txt"))
