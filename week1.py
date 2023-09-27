words = ['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']


def front_x(words):
    x_first = [word for word in words if word[0] == 'x']
    x_not_first = [word for word in words if len(word) < 1 continue elif word[0] != 'x']
    return sorted(x_first) + sorted(x_not_first)


print(front_x(words))