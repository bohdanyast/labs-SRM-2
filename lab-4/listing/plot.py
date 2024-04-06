from matplotlib import pyplot as plt
import numpy as np
from math import sqrt

def f(x):
    return x ** 3 * sqrt(x ** 2 - 49)

def plot():
    plt.grid(True)

    x = np.linspace(7, 10, 10**6)
    y = [f(i) for i in x]

    plt.axvline(7.5, color="orange")
    plt.axvline(9.5, color="orange")
    plt.axhline(0, color="orange")

    plt.plot(x, y)

    plt.fill_between(x, y, where=((x >= 7.5) & (x <= 9.5)), color='orange', alpha=0.3)

    plt.show()


plot()
