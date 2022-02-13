import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate (word):
    word_forms = [word.lower(), word.upper(), word.capitalize()]
    w = word_forms[0]
    for words in word_forms:
        if words in data:
            return data[words]
    

    if get_close_matches(w, data.keys(), cutoff = 0.75): #This method compares strings to find their similarities
        new_w = get_close_matches(w, data.keys(), cutoff = 0.75)

        yn = input (f"Did you mean {new_w[0]} instead? Enter Y if yes, N if no ..." ) 
        if yn == "Y" or yn == "y":
            return data[new_w[0]]   
        elif yn == "N" or yn == "n" :
            return "The word doesn't exist. Please double check it"
        else:
            return "Entry not valid"

    else:
        return "The word doesn't exist. Please double check it"

word = input("Enter word: ") 
output = translate(word)


if type(output) is list:
    print (f"The word has {len(output)} meaning \n")
    for i, item in enumerate(output, start = 1):
         print (i,") ", item,sep = "")
else:
    print (output)
    