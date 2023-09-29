from string import ascii_uppercase as eng_alphabet

def text_formatter(text):
    return ''.join(x for x in text.upper() if x.isalpha() or x.isdigit())

def generate_rotors():
    rotors_list = [
       'A 	B 	C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N 	O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z',
        'E 	K 	M 	F 	L 	G 	D 	Q 	V 	Z 	N 	T 	O 	W 	Y 	H 	X 	U 	S 	P 	A 	I 	B 	R 	C 	J',
        'A 	J 	D 	K 	S 	I 	R 	U 	X 	B 	L 	H 	W 	T 	M 	C 	Q 	G 	Z 	N 	P 	Y 	F 	V 	O 	E',
        'B 	D 	F 	H 	J 	L 	C 	P 	R 	T 	X 	V 	Z 	N 	Y 	E 	I 	W 	G 	A 	K 	M 	U 	S 	Q 	O',
        'E 	S 	O 	V 	P 	Z 	J 	A 	Y 	Q 	U 	I 	R 	H 	X 	L 	N 	F 	T 	G 	K 	D 	C 	M 	W 	B',
        'V 	Z 	B 	R 	G 	I 	T 	Y 	U 	P 	S 	D 	N 	H 	L 	X 	A 	W 	M 	J 	Q 	O 	F 	E 	C 	K',
        'J 	P 	G 	V 	O 	U 	M 	F 	Y 	Q 	B 	E 	N 	H 	Z 	R 	D 	K 	A 	S 	X 	L 	I 	C 	T 	W',
        'N 	Z 	J 	H 	G 	R 	C 	X 	M 	Y 	S 	W 	B 	O 	U 	F 	A 	I 	V 	L 	P 	E 	K 	Q 	D 	T',
        'F 	K 	Q 	H 	T 	L 	X 	O 	C 	B 	J 	S 	P 	D 	Z 	R 	A 	M 	E 	W 	N 	I 	U 	Y 	G 	V',
        'L 	E 	Y 	J 	V 	C 	N 	I 	X 	W 	P 	B 	Q 	M 	D 	R 	T 	A 	K 	Z 	G 	F 	U 	H 	O 	S',
        'F 	S 	O 	K 	A 	N 	U 	E 	R 	H 	M 	B 	T 	I 	Y 	C 	W 	L 	Q 	P 	Z 	X 	V 	G 	J 	D'
    ]
    rotors = { i: (rotors_list[i]).split(' 	') for i in range(8) }
    rotors['beta'], rotors['gamma'] = rotors_list[8].split(' 	'), rotors_list[9].split(' 	')
    return rotors

def generate_reflectors():
    reflectors_list = [
        '(AY) (BR) (CU) (DH) (EQ) (FS) (GL) (IP) (JX) (KN) (MO) (TZ) (VW)',
        '(AF) (BV) (CP) (DJ) (EI) (GO) (HY) (KR) (LZ) (MX) (NW) (TQ) (SU)',
        '(AE) (BN) (CK) (DQ) (FU) (GY) (HW) (IJ) (LO) (MP) (RX) (SZ) (TV)',
        '(AR) (BD) (CO) (EJ) (FN) (GT) (HK) (IV) (LM) (PW) (QZ) (SX) (UY)'
    ]
    
    reflectors_list = [reflector[1:-1].split(') (') for reflector in reflectors_list]
    return reflectors_list

    
def rotor(symbol, n, reverse=False): 
    rotors = generate_rotors()
    if reverse:
        return rotors[0][rotors[n].index(symbol)]
    else:
        return rotors[n][rotors[0].index(symbol)]

def reflector(symbol, n):
    reflectors_list = generate_reflectors()
    if n > 0:
        for pair in reflectors_list[n - 1]:
            if pair[0] == symbol:
                return pair[1]
            elif pair[1] == symbol:
                return pair[0]
    else:
        return symbol

def enigma_v01(text, ref, rot1, rot2, rot3):
    result = ''
    rot_list = [rot3, rot2, rot1]
    for symbol in text_formatter(text):
        for rot in rot_list:
            symbol = rotor(symbol, rot)
        symbol = reflector(symbol, ref)
        for rot in reversed(rot_list):
            symbol = rotor(symbol, rot, True)
        result += symbol
    return result

def caesar(text, key, alphabet=eng_alphabet):
    encrypted = ''
    for letter in text_formatter(text):
        cursor = alphabet.find(letter) + key
        while abs(cursor) > len(alphabet) - 1:
            cursor = cursor - int(key/abs(key)) * len(alphabet)
        encrypted += alphabet[cursor]
    return encrypted

def shifter(symbol, rotors, reverse=False):
    prev_shift = 0
    for rot in rotors[::-1] if reverse else rotors: 
        symbol = caesar(symbol, rot['shift'] + prev_shift)
        symbol = rotor(symbol, rot['rot'], reverse)
        prev_shift = -rot['shift']
    return caesar(symbol, prev_shift)

def check_shift(symbol, rot):
    rotors_shift = {1: 'R', 2: 'F', 3: 'W', 4: 'K',
                    5: 'A', 6: 'AN', 7: 'AN', 8: 'AN'}
    return rotors_shift[rot] == symbol

def shifter_v03(symbol, rotors, reverse=False):
    prev_shift = 0
    for rot in rotors[::-1] if reverse else rotors: 
        symbol = caesar(symbol, rot['shift'] + prev_shift)
        symbol = rotor(symbol, rot['rot'], reverse)
        prev_shift = -rot['shift']
        process_shift += 1
    return caesar(symbol, prev_shift)

def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    result = ''
    rotors = [
        {'rot': rot3, 'shift': shift3},
        {'rot': rot2, 'shift': shift2},
        {'rot': rot1, 'shift': shift1}
    ]
    for symbol in text_formatter(text):
        symbol = shifter_v03(symbol, rotors)
        symbol = reflector(symbol, ref)
        symbol = shifter_v03(symbol, rotors, True)
        result += symbol
    return result

tests = [
    enigma('AAAAAAA', 1, 1, 0, 2, 0, 3, 0),
    enigma('BDZGOWC', 1, 1, 0, 2, 0, 3, 0),
    enigma('AAAAAAA', 1, 2, 3, 2, 3, 2, 3),
    enigma('AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA', 1, 2, 3, 2, 3, 2, 3),
    enigma('AAAAA AAAAA', 1, 1, 0, 2, 0, 2, 0),
    enigma('AAAAA AAAAA', 1, 1, 0, 2, 0, 1, 0)
]

[print(test) for test in tests]
