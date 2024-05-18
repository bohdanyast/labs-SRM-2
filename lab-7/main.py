import numpy as np


def system(x, a):
    f1 = x[0]**2 - 2 * np.log10(x[1]) - 1
    f2 = x[0]**2 - a * x[0] * x[1] + a

    return np.array([f1, f2], dtype=float)


def jacobi_matrix(x, a):
    df1_dx1 = 2 * x[0]
    df1_dx2 = 2 / (np.log(10)*x[1])
    df2_dx1 = 2 * x[0]
    df2_dx2 = -a * x[0]
    return np.array([[df1_dx1, df1_dx2],
                    [df2_dx1, df2_dx2]], dtype=float)


def newton_method(x0, a, eps):
    x = x0.copy()
    while True:
        dx = np.linalg.solve(jacobi_matrix(x0, a), -system(x, a))
        x += dx
        if np.linalg.norm(dx) < eps:
            break
    return x


def simple_iteration_method(x0, a, eps):
    x = x0.copy()
    while True:
        x1_next = np.sqrt(1 + 2 * np.log10(x[1]))
        x2_next = (x[0]**2 + a) / (a * x[0])
        x_next = np.array([x1_next, x2_next])
        if abs(np.linalg.norm(x - x_next)) < eps:
            break
        x = x_next
    return x


x0 = np.array([1.5, 1.5], dtype=float)
eps = 0.00001
a = 6


print("Метод Ньютона:", newton_method(x0, a, eps))
print("Метод простої ітерації:", simple_iteration_method(x0, a, eps))
