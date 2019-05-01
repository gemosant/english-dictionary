import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Bunu mu kastettin: %s? Evet ise Y, değil ise N gir: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Kelimeyi bulamadım. Lütfen tekrar kontrol et."
        else:
            return "Girdiğin cevabı anlayamadım."
    else:
        return "Kelimeyi bulamadım. Lütfen tekrar kontrol et."

word = input("Kelime gir: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)