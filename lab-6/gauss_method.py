import numpy as np

# matrix of system of linear equations to solve with Gauss method and to count the determinant and reversed matrix

gauss_matrix = [
    [9, -5, -6, 3],
    [1, -7, 1, 0],
    [3, -4, 9, 0],
    [6, -1, 9, 8],
]

gauss_solves = [-8, 38, 47, -8]


def solve_by_gauss_method(coef_matrix, solving_matrix):
    coef_matrix = np.array(coef_matrix, dtype=float)
    solving_matrix = np.array(solving_matrix, dtype=float)

    reshaped_solving_matrix = solving_matrix.reshape((len(solving_matrix), 1))
    coef_matrix = np.hstack((coef_matrix, reshaped_solving_matrix))

    for i in range(len(coef_matrix)):
        for j in range(i + 1, len(coef_matrix)):
            coef_matrix[j] -= coef_matrix[i] * coef_matrix[j][i] / coef_matrix[i][i]

    x = np.array([0] * len(solving_matrix), dtype=float)

    i = len(coef_matrix) - 1
    while i >= 0:
        x[i] = (coef_matrix[i][-1] - sum(x * coef_matrix[i][0:-1])) / coef_matrix[i][i]
        i -= 1

    return x.astype(int)


def get_determinant(coef_matrix, solving_matrix):
    det = 1

    coef_matrix = np.array(coef_matrix, dtype=float)
    solving_matrix = np.array(solving_matrix, dtype=float)

    reshaped_solving_matrix = solving_matrix.reshape((len(solving_matrix), 1))
    coef_matrix = np.hstack((coef_matrix, reshaped_solving_matrix))

    for i in range(len(coef_matrix)):
        for j in range(i + 1, len(coef_matrix)):
            coef_matrix[j] -= coef_matrix[i] * coef_matrix[j][i] / coef_matrix[i][i]

    for k in range(len(coef_matrix[0])-1):
        det *= coef_matrix[k][k]

    return det


def get_reversed_matrix(coef_matrix):
    coef_matrix = np.array(coef_matrix, dtype=float)

    n = coef_matrix.shape[0]
    augmented_matrix = np.hstack((coef_matrix, np.eye(n)))

    for i in range(n):
        divisor = augmented_matrix[i][i]
        augmented_matrix[i] /= divisor
        for j in range(n):
            if i != j:
                multiplier = augmented_matrix[j][i]
                augmented_matrix[j] -= multiplier * augmented_matrix[i]

    inverse_matrix = augmented_matrix[:, n:]

    return inverse_matrix