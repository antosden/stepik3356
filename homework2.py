from random import choice

def mimic_dict(string):
    words = string.split()
    dictonary = {"": []}
    prev_word = ""
    for word in words:
        dictonary[prev_word].append(word)
        if word not in dictonary.keys() and words.index(word) != len(words) - 1:
            dictonary[word] = []
        prev_word = word
    return print_mimic(dictonary, dictonary[""][0])

def print_mimic(mimic_dict, word):
    result = [word]
    while len(result) < 200:
        if word not in mimic_dict.keys():
            word = choice(mimic_dict[''])
            result.append(word)
        cur_word = choice(mimic_dict[word])
        result.append(cur_word)
        word = cur_word
    return ' '.join(result)

string = """
We are not what we should be
We are not what we need to be
But at least we are not what we used to be
  -- Football Coach
"""

print(mimic_dict(string))