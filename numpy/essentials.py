import numpy as np

def line_segment_len(A, B):
    return sum(np.array(A - B) ** 2) ** 0.5

def triangle_area(A1, A2, A3):
    A = line_segment_len(A1, A2)
    B = line_segment_len(A2, A3)
    C = line_segment_len(A3, A1)

    p = 0.5 * (A + B + C)
    return (p * (p - A) * (p - B) * (p - C)) ** 0.5


M1 = np.array((
    (1., 2., 3., 0.),
    (4., 5., 6., 0.),
    (0., 1., 1., 6.),
    (7., 8., 9., 0.)
))

def matrix_operations(M):
    M[-2] = np.sin(M[-2] * np.pi/6)
    M[:, -2] = np.exp(M[:, -2])
    return M

def create_zero_matrix(data):
    try:
        shape, dtype = [int(x) for x in data], np.float64
    except:
        shape, dtype = [int(x) for x in data[:-1]], data[-1]
    finally:
        return np.zeros(shape, dtype)