def simple_multiplication(x, y):
    first_numbers = (100 - ((100 - x) + (100 - y))) * 100
    second_numers = (100 - x) * (100 - y)
    result = first_numbers + second_numers
    return result

def multiplication_check(x, y, length_check):
    true_result = x * y
    # sage_result = simple_multiplication(x, y)
    sage_result = wisdom_multiplication(x, y, length_check)
    return true_result == sage_result

def multiplication_check_list_old(start=10, stop=99):
    result = []
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            result.append(multiplication_check(x, y))
    print('Правильных результатов: %s' % (result.count(True)))
    print('Неправильных результатов: %s' % (result.count(False)))

def wisdom_multiplication(x, y, length_check = True):
    first_numbers = str(100 - ((100 - x) + (100 - y)))
    second_numers = str((100 - x) * (100 - y))
    if length_check and len(second_numers) < 2:
        second_numers = '0' + second_numers
    result = int(first_numbers + second_numers)
    return result

def multiplication_check_list(start=10, stop=99, length_check = True):
    result = []
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            result.append(multiplication_check(x, y, length_check))
    print('Правильных результатов: %s' % (result.count(True)))
    print('Неправильных результатов: %s' % (result.count(False)))

multiplication_check_list()