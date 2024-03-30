import numpy as np


def cubic_spline_coefficients(x, y):
    n = len(x)
    h = np.diff(x)

    # запис індексів матриць через кому в numpy ідентичний звичайному matrix[i][i-1]
    matrix = np.zeros((n, n))
    matrix[0, 0] = 1
    matrix[-1, -1] = 1

    for i in range(1, n - 1):
        matrix[i, i - 1] = h[i - 1]
        matrix[i, i] = 2 * (h[i - 1] + h[i])
        matrix[i, i + 1] = h[i]


    rhs = np.zeros(n)
    for i in range(1, n - 1):
        rhs[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    second_derivatives = np.linalg.solve(matrix, rhs)

    # формули коефіцієнтів сплайну з відкритих джерел
    coefficients = []
    for i in range(n - 1):
        a = y[i]
        b = (y[i + 1] - y[i]) / h[i] - h[i] / 3 * (2 * second_derivatives[i] + second_derivatives[i + 1])
        c = second_derivatives[i]
        d = (second_derivatives[i + 1] - second_derivatives[i]) / (3 * h[i])
        coefficients.append([a, b, c, d])

    return coefficients


def spline_interpolation(x_vals, y_vals):
    coefficients = cubic_spline_coefficients(x_vals, y_vals)
    return coefficients


x_vals = [-2.2, -1.2, -0.2, 0.8, 1.8]
y_vals = [-0.27067, -0.36788, 0.0, 2.7183, 14.778]

coefficients = spline_interpolation(x_vals, y_vals)
for i, coef in enumerate(coefficients):
    xi = x_vals[i]
    xi_next = x_vals[i + 1]

    interval_title = f"[{xi}, {xi_next}]"
    polynomial = f"{coef[0]:.3f} + {coef[1]:.3f}(x - {xi}) + {coef[2]:.3f}(x - {xi})**2 + {coef[3]:.3f}(x - {xi})**3"

    print(f"{interval_title}: {polynomial}")


def count_value(x):
    if -2.2 <= x <= -1.2:
        return -0.271 - 0.221*(x + 2.2) + 0.000*(x + 2.2)**2 + 0.124*(x + 2.2)**3
    elif -1.2 <= x <= -0.2:
        return -0.368 + 0.150*(x + 1.2) + 0.371*(x + 1.2)**2 - 0.152*(x + 1.2)**3
    elif -0.2 <= x <= 0.8:
        return -0.000 + 0.434*(x + 0.2) - 0.087*(x + 0.2)**2 + 2.371*(x + 0.2)**3
    elif 0.8 <= x <= 1.8:
        return 2.178 + 7.375*(x - 0.8) + 7.028*(x - 0.8)**2 - 2.343*(x - 0.8)**3


x = -0.5
print(f"Значення в х = {x}: {count_value(x)}")
