alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert(num, to_base=10, from_base=10):
    if from_base != 10 or to_base == 10:
        num = to_decimal(str(num), from_base)
    return num if to_base==10 else to_numeral_system(int(num), to_base)   

def to_decimal(num, from_base):
    result = 0
    i = len(num) - 1
    for n in num:
        result += (n if type(n) is int else alphabet.find(n)) * from_base**i 
        i -= 1
    return result

def to_numeral_system(num, to_base):
    result = ''
    while num >= to_base:
        result += alphabet[num % to_base]
        num = num // to_base
    if num > 0:
        result += alphabet[num]

    return result[::-1]

def kaprekar(n, base = 10):
    result = False
    prod = to_numeral_system((to_decimal(str(n), base)**2), base)
    for i in range(1, len(prod)):
        a, b = to_decimal(prod[:i], base), to_decimal(prod[i:], base)
        if a == 0 or b == 0:
            continue
        sum = to_numeral_system(a + b, base)
        if sum == str(n):
            result = True
            break
    return result


test_1 = [9, 45, 55, '99', '297', 703, 999, '2223', 2728, '4879']
test_2 = [10, 46, 56, 100, 298, 704, '1000', '2224', '2729', '4880']
test_3 = ['6', 'A', 'F', '33', '55', '5B', '78', '88', 'AB', 'CD', 'FF', '15F', '334', '38E']

# print(kaprekar(9))

print([kaprekar(i) for i in test_1]) # Тест чисел Капрекара из системы с основанием 10

print([kaprekar(i) for i in test_2 ]) # Тест НЕ чисел Капрекара из системы с основанием 10

print([kaprekar(i, base=16) for i in test_3]) #Тест чисел Капрекара из системы с основанием 16