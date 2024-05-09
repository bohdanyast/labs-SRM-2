import numpy as np


def iterative_method(coef_matrix, solve_matrix, eps):
    coef_matrix = np.array(coef_matrix, dtype=float)
    solve_matrix = np.array(solve_matrix, dtype=float)

    alpha = -coef_matrix / coef_matrix.diagonal().reshape(coef_matrix.shape[0], 1)
    np.fill_diagonal(alpha, 0)

    beta = solve_matrix / coef_matrix.diagonal()

    results_list = []

    x_prev = solve_matrix
    while True:
        x = beta + np.dot(alpha, x_prev)

        results_list.append(x)

        if np.all(np.abs(x - x_prev) < eps):
            return x
        else:
            x_prev = x