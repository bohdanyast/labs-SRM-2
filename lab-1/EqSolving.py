from math import *


# setting an equation according to variant for requiring methods
def f(x):
    return 3 ** x - x ** 3 - 3


# first derivative of f(x)
def df(x):
    return 3 ** x * log(3) - 3 * x ** 2


# x = g(x) implementation for easier SI-method
def g(x):
    return cbrt(3 ** x - 3)


# bisection method (half-dividing)
def bisection_method(a, b, eps):
    if f(a) * f(b) > 0:
        print("f(a) and f(b) have the same sign")
        return None

    while (b - a) > 2 * eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# chord method
def chord_method(a, b, epsilon):
    x1 = a
    while True:
        if f(a) * f(b) > 0:
            print("f(a) and f(b) have the same sign")
            return None
        a_values = f(a)
        b_values = f(b)
        x2 = a - (a_values * (a - b)) / (a_values - b_values)
        c_values = f(x2)
        if abs(x1 - x2) < epsilon:
            return x2
        if (a_values * c_values) < 0:
            b = x2
        else:
            a = x2
        x1 = x2


# newton method
def newton_method(start, epsilon):
    x = start
    while True:
        x1 = x - f(x) / df(x)
        x = x1
        if abs(x - x1) < epsilon:
            break
        if df(x) == 0:
            return "division by zero"

    return x1


# simple iteration method, we are required to get g(x) function and x in left
def simple_iteration_method(approx, epsilon):
    x = approx
    while True:
        x1 = g(x)
        x = x1
        if abs(x - x1) < epsilon:
            break

    return x


print(f"Метод половинного ділення: {bisection_method(0, 4, 0.00001)}")
print("-"*20)

print(f"Метод хорд: {chord_method(2, 4, 0.00001)}")
print("-"*20)

print(f"Метод Ньютона: {newton_method(3.43, 0.00001)}")
print("-"*20)

print(f"Метод простої ітерації: {simple_iteration_method(3.434, 0.00001)}")