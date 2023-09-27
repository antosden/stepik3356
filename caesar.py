from string import ascii_uppercase as eng_alphabet

def caesar(text, key, alphabet=eng_alphabet):
    text = ''.join(x for x in text.upper() if x.isalpha() or x.isdigit())
    encrypted = ''
    for letter in text:
        cursor = alphabet.find(letter) + key
        while abs(cursor) > len(alphabet) - 1:
            cursor = cursor - int(key/abs(key)) * len(alphabet)
        
        encrypted += alphabet[cursor]
    return encrypted

def bruteforce(text, alphabet=eng_alphabet):
    for key in reversed(range(1, len(alphabet))):
        print(caesar(text, key, alphabet))

def jarriquez_encryption(text, key, alphabet=eng_alphabet, reverse=False):
    text = ''.join(x for x in text.upper() if x.isalpha() or x.isdigit())
    encrypted = ''
    for letter, num in text, key:
        encrypted += caesar(letter, num, alphabet)

    pass
