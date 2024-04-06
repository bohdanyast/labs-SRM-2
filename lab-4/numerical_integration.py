from math import sqrt
import numpy as np


x1 = 7.5
x2 = 9.5
h1 = 0.5
h2 = 0.25
global_result = 6165.7819


def f(x):
    return x ** 3 * sqrt(x ** 2 - 49)


def rectangular_method(h):
    area = 0
    n = np.arange(x1, x2, h)
    for i in n:
        area += f(i + h/2)*h
    return area


def trapezoidal_method(h):
    area = (f(x1) + f(x2))
    n = np.arange(x1, x2, h)
    for i in n[1:]:
        area += 2*f(i)
    return area * h/2


def simpson_method(h):
    area = (f(x1) + f(x2))
    n = np.arange(x1, x2, h)
    for i in range(1, len(n)):
        if i % 2 == 1:
            area += 4*f(n[i])
        else:
            area += 2*f(n[i])
    return area * h/3


def runge_check(result_h, result_half_h, p):
    result = result_half_h - (result_half_h - result_h)/(2**p - 1)
    return result


print(f"h = {h1}:")
print(rectangular_method(h1), trapezoidal_method(h1), simpson_method(h1), sep="\n")

print("-"*20)

print(f"h = {h2}:")
print(rectangular_method(h2), trapezoidal_method(h2), simpson_method(h2), sep="\n")

print("-"*20)

print("Уточнення Рунге з кроками h i h/2")
print(f"Метод прямокутників: {runge_check(rectangular_method(h1), rectangular_method(h2), 4)}")
print(f"Метод трапецій: {runge_check(trapezoidal_method(h1), trapezoidal_method(h2), 4)}")
print(f"Метод Сімпсона: {runge_check(simpson_method(h1), simpson_method(h2), 4)}")