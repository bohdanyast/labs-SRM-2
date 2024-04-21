import numpy as np
import matplotlib.pyplot as plt

# Given data arrays
x_arr = [round(i, 1) for i in np.arange(0, 1.1, 0.1)]
euler_method_arr = [3, 3.0, 3.06, 3.1804, 3.36367, 3.61449, 3.94009, 4.35082, 4.86099, 5.49017, 6.26512]
euler_koshi_method_arr = [3, 3.03, 3.1205, 3.27414, 3.49575, 3.79265, 4.17519, 4.65753, 5.25882, 6.00493, 6.93106]
runge_kutta_method_arr = [3, 3.03008, 3.12124, 3.27641, 3.50079, 3.80226, 4.19198, 4.68527, 5.30304, 6.07376, 7.03655]
exact_vals_arr = [3.0, 3.03008, 3.12135, 3.27689, 3.50214, 3.80521, 4.19758, 4.69501, 5.31897, 6.09877, 7.07465]

# Plotting the curves
plt.plot(x_arr, euler_method_arr, label='Euler Method', color='blue')
plt.plot(x_arr, euler_koshi_method_arr, label='Euler-Koshi Method', color='green')
plt.plot(x_arr, runge_kutta_method_arr, label='Runge-Kutta Method', color='yellow')
plt.plot(x_arr, exact_vals_arr, label='Exact Values', color='red')

# Adding labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Different Methods')

# Adding legend
plt.legend()

# Display the plot
plt.show()
