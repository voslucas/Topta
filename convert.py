import os
import whisper
import json

# get a list of all mp3 files
def get_mp3_files():
    mp3_files = []
    for file in os.listdir('.'):
        if file.endswith('.mp3'):
            mp3_files.append(file)
    return mp3_files

# Use the OpenAI Whisper API to convert the mp3 files to txt
def convert_mp3_to_txt(mp3_file, model):
    print("Converting", mp3_file)
    result = model.transcribe(mp3_file, language="nl",  verbose=False)
    return json.dumps(result, indent=2)
    #return result["text"]


# for each mp3 file , check if there is a txt file with the same name
# if not convert the mp3 file to txt
def convert_all_mp3_files():
    mp3_files = get_mp3_files()
    model = whisper.load_model("large", device="cuda")
    for mp3_file in mp3_files:
        json_file = mp3_file.replace(".mp3", ".json")
        if not os.path.exists(json_file):
            json_text = convert_mp3_to_txt(mp3_file, model)
            with open(json_file, "w",  encoding='utf-8') as f:
                f.write(json_text)
        else:
            print("Already converted", mp3_file)
    print("All mp3 files converted")


convert_all_mp3_files()
