import numpy as np


def seidel_method(coef_matrix, solve_matrix, eps):
    n = len(coef_matrix)
    x = np.zeros(n)
    while True:
        x_new = np.zeros(n)
        for i in range(n):
            s1 = sum(coef_matrix[i][j] * x_new[j] for j in range(i))
            s2 = sum(coef_matrix[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (solve_matrix[i] - s1 - s2) / coef_matrix[i][i]
        if np.linalg.norm(x_new - x) < eps:
            break
        x = x_new
    return x
