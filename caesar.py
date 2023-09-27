from string import ascii_uppercase as eng_alphabet
from random import shuffle, seed

jarriquez_text = """ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕ

ЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБ

САОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖО

ИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС"""

ru_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def caesar(text, key, alphabet=eng_alphabet):
    encrypted = ''
    for letter in text_formatter(text):
        cursor = alphabet.find(letter) + key
        while abs(cursor) > len(alphabet) - 1:
            cursor = cursor - int(key/abs(key)) * len(alphabet)
        encrypted += alphabet[cursor]
    return encrypted

def bruteforce(text, alphabet=eng_alphabet, jarriquez=False):
    if jarriquez:
        key = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(key)
        key = ''.join(str(x) for x in key)
        return jarriquez_encryption(text, key, alphabet, reverse=True)
    else:
        for key in reversed(range(1, len(alphabet))):
            print(caesar(text, key, alphabet))

def text_formatter(text):
    return ''.join(x for x in text.upper() if x.isalpha() or x.isdigit())

def jarriquez_encryption(text, key, alphabet=eng_alphabet, reverse=False):
    encrypted = ''
    key_index = 0
    key = str(key)
    for letter in text_formatter(text):
        encrypted += caesar(letter, -int(key[key_index]), alphabet) if reverse else caesar(letter, int(key[key_index]), alphabet)
        key_index = key_index + 1 if key_index < len(key) - 1 else 0
    return encrypted

def frequency_analysis(text):
    frequency = dict()
    for letter in text:
        if letter not in frequency.keys():
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    return sorted(frequency.items(), key=lambda item: item[1])

# TODO: Реализовать алгоритм расшифровки с использованием частотного анализа

def jarriquez_bruteforce(text):
    keys = [int(x) for x in range (8600, 999999)]
    for key in keys:
        # print('key: %s' % key)
        decrypted = jarriquez_encryption(text, str(key), alphabet=ru_alphabet, reverse=True)
        if 'ДАКОСТА' in decrypted and 'АЛМАЗ' in decrypted:
            print('Найдено совпадение по словам!')
            print(key)
            print(decrypted)


def disc_generator(alphabet):
    seed(42)
    alphabet = [str(x) for x in alphabet]
    shuffle(alphabet)
    alphabet = ''.join(str(x) for x in alphabet)
    return alphabet


def jefferson_encryption(text, discs, step, reverse=False):
    index = 0
    result = ''
    for letter in text_formatter(text):
        result += caesar(letter, -step, discs[index]) if reverse else caesar(letter, step, discs[index])
        index = index + 1 if index < len(discs) - 1 else 0
    return result
    
def kidds_encryption(text, reverse=False):
    result = ''
    if not reverse:
        text = (text_formatter(text)).lower()
    for letter in text:
        if reverse:
            result += dictonary[letter]
        else:
            for key, value in dictonary.items():
                if dictonary[key] == letter:
                    result += key
                    break
            
    return result


a = "8 	; 	4 	‡ 	) 	* 	5 	6 	( 	1 	† 	0 	9 	2 	: 	3 	? 	¶ 	- 	.".split(' 	')
b = "e 	t 	h 	o 	s 	n 	a 	i 	r 	f 	d 	l 	m 	b 	y 	g 	u 	v 	c 	p". split(' 	')

dictonary = dict()
for i in range(len(a)):
    dictonary[a[i]] = b[i]

encrypted = (kidds_encryption('ethosnairfdlmbyguvcp'))
decrypted = (kidds_encryption(encrypted, True))

print(encrypted, decrypted)