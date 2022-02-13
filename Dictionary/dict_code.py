import json
from difflib import SequenceMatcher

data = json.load(open("data.json"))  #open the json data and loads it.
print(type(data))

def define(word):
    try:
        return data[word.lower()]
            
    except :
        return ("Word not in the dictionary")

#search = input("Enter word ...:")
#for s in define(search):
#    print("-", s)
