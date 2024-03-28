import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

x = np.array([-2.2, -1.2, -0.2, 0.8, 1.8])
y = np.array([-0.27067, -0.36788, 0.0, 2.7183, 14.778])

cs = CubicSpline(x, y)

x_interp = np.linspace(min(x), max(x), 100)
y_interp = cs(x_interp)

plt.scatter(x, y, label='Original Data')
plt.plot(x_interp, y_interp, label='Cubic Spline Interpolation')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cubic Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()
