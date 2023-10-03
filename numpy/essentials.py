import numpy as np

def task_01():
    # numbers = [float(x) for x in "1, 2, 3, 4, 5.0, 6, 7, 8, 9, 10".split(', ')]
    numbers = [float(x) for x in input().split(', ')]

    V1 = np.array(numbers)
    V2 = np.array([numbers[-2]])
    V3 = np.array(numbers[::-1])
    V4 = np.array(numbers[0::3])
    V5 = np.array(range(len(numbers)))

    tests = [V1, V2, V3, V4, V5]
    [print(test) for test in tests]

def task_02():
    V1 = np.array([int(x) for x in input().split(', ')])
    V2 = np.array([int(x) for x in input().split(', ')])
    V3 = V1 + V2
    V4 = (V1[::-1])[::1] * (V2[::-1])[::1]
