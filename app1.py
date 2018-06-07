import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:                             #incase user inputs a proper noun
        return data[w.title()]
    elif w.upper() in data:                             #incase user inputs acronyms like USA, UAE etc
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:     #for matching words
        yn=input("Did you mean %s instead?\n Enter Y for yes and N for no: " % get_close_matches(w,data.keys())[0])
        yn=yn.lower()
        if yn=='y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=='n':
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your query"
    else:
        return "The word doesn't exist.Please double check it"

word=input("Enter a word: ")

object = translate(word)

if type(object)==list:
    for i in object:
        print(i)
else:
    print(object)
