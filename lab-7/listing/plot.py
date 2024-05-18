import numpy as np
from matplotlib import pyplot as plt


x = np.linspace(0, 10)
x1 = np.sqrt(1 + 2 * np.log10(x))
x2 = (x**2 + 6) / (6 * x)
plt.plot(x1, x, x, x2)
plt.show()
plt.close()
