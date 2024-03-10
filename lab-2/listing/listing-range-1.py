import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f(x):
    return np.sin(x) + np.exp(x)

def l(x):
    return 0.835 * x**3 - 1.415 * x**2 + 3.14 * x + 1

# Define x values
x_vals = np.linspace(0, 3.5, 1000)  # Adjust the range as needed for your plot

# Compute y values for each function
y_f = f(x_vals)
y_l = l(x_vals)

# Highlighted dots
x1_vals = [0, 1, 2, 3]
y1_vals = [1, 3.56, 8.3, 20.23]

# Plot the functions
plt.plot(x_vals, y_f, label='f(x) = sin(x) + e^x')
plt.plot(x_vals, y_l, label='l(x) = 0.835*x^3 - 1.415*x^2 + 3.14*x + 1')

# Highlight the specified dots
plt.scatter(x1_vals, y1_vals, color='red', label='Highlighted Dots')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.title('Graphs of f(x) and l(x) with Highlighted Dots')
plt.grid(True)
plt.show()
