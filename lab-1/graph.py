import numpy as np
import matplotlib.pyplot as plt

# our f(x)
def func(x):
    return 3**x - x**3 - 3


x_values = np.arange(-1.7, 3.6, 0.1)
y_values = func(x_values)

# building a graph
plt.plot(x_values, y_values, label='3**x - x**3 - 3')

# title + axes titles
plt.title('Func. 3**x - x**3 - 3')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)
plt.legend()
plt.show()
