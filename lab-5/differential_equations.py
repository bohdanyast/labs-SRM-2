from math import sqrt, e
import numpy as np
from prettytable import PrettyTable, ALL

# Initial conditions
y, dy = 3, 0
x1, x2 = 0, 1
h = 0.1

# Generate x values
x_arr = [round(i, 1) for i in np.arange(x1, x2 + h, h)]


# Differential equation
def dif_eq_2(x, y, dy):
    return 4 * x ** 2 * e ** (x ** 2) + 2 * y + 0 * dy


# Precise function for comparison
def y_exact(x):
    return e ** (x ** 2) + e ** (x * sqrt(2)) + e ** (-x * sqrt(2))


# Get exact solution for the given differential equation
def get_exact_vals(x_arr):
    return [round(y_exact(i), 5) for i in x_arr]


# Euler method (usual)
def euler_method(x1, x2, h, y0, dy0):
    x_values = np.arange(x1, x2 + h, h)
    y_values = [y0]
    dy_values = [dy0]

    for i in range(1, len(x_values)):
        x_prev, y_prev, dy_prev = x_values[i - 1], y_values[i - 1], dy_values[i - 1]
        dy_new = dy_prev + h * dif_eq_2(x_prev, y_prev, dy_prev)
        y_new = y_prev + h * dy_prev
        y_values.append(round(y_new, 5))
        dy_values.append(round(dy_new, 5))

    return y_values


# Euler-Koshi method (usual)
def euler_koshi_method(x1, x2, h, y0, dy0):
    x_values = np.arange(x1, x2 + h, h)
    y_values = [y0]
    dy_values = [dy0]

    for i in range(1, len(x_values)):
        x_prev, y_prev, dy_prev = x_values[i - 1], y_values[i - 1], dy_values[i - 1]
        _y = y_prev + h * dy_prev
        _dy = dy_prev + h * dif_eq_2(x_prev, y_prev, dy_prev)
        y_new = y_prev + h / 2 * (_dy + dy_prev)
        dy_new = dy_prev + h / 2 * (dif_eq_2(x_prev, y_prev, dy_prev) + dif_eq_2(x_prev, _y, _dy))
        y_values.append(round(y_new, 5))
        dy_values.append(round(dy_new, 5))

    return y_values


# runge-kutta method
def runge_kutta_method(x1, x2, h, y0, dy0):
    arr = []
    while x1 <= x2:
        arr.append(round(y0, 5))
        k1 = h * dy0
        l1 = h * dif_eq_2(x1, y0, dy0)
        k2 = h * (dy0 + l1 / 2)
        l2 = h * dif_eq_2(x1 + h / 2, y0 + k1 / 2, dy0 + l1 / 2)
        k3 = h * (dy0 + l2 / 2)
        l3 = h * dif_eq_2(x1 + h / 2, y0 + k2 / 2, dy0 + l2 / 2)
        k4 = h * (dy0 + l3)
        l4 = h * dif_eq_2(x1 + h / 2, y0 + k3 / 2, dy0 + l3 / 2)

        delta_y = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y0 += delta_y
        delta_z = (l1 + 2 * l2 + 2 * l3 + l4) / 6
        dy0 += delta_z
        x1 += h
    return arr


# get pretty table of solving
def get_pretty_table_result(x_arr, y_arr, y_precise_arr):
    my_table = PrettyTable(['x'] + x_arr)
    my_table.hrules = ALL
    my_table.add_row(['y'] + y_arr)
    my_table.add_row(['y (іст.)'] + y_precise_arr)
    my_table.add_row(['ε'] + [round(y_p - y, 5) for y_p, y in zip(y_precise_arr, y_arr)])

    print(my_table)


# get table of erros
# def get_pretty_table_errors()


print("Метод Ейлера:")
get_pretty_table_result(x_arr, euler_method(x1, x2, h, y, dy), get_exact_vals(x_arr))
print('\n'*2)

print("Метод Ейлера-Коші:")
get_pretty_table_result(x_arr, euler_koshi_method(x1, x2, h, y, dy), get_exact_vals(x_arr))
print('\n'*2)

print("Метод Рунге-Кутти:")
get_pretty_table_result(x_arr, runge_kutta_method(x1, x2, h, y, dy), get_exact_vals(x_arr))
print('\n'*2)



