import numpy as np

# параметри
h = 0.2
x = np.arange(1.1, 2.1 + h, h)
n = len(x)

# Create the coefficient matrix and RHS vector
A = np.zeros((n, n))
b = np.zeros(n)

# Boundary condition at x = 1.1 for y'(1.1) = 1.5
A[0, 0] = -1 / (2*h)
A[0, 1] = 1 / (2*h)
b[0] = 1.5

# Interior points
for i in range(1, n-1):
    xi = x[i]
    A[i, i-1] = 1 / h**2 - xi / (2*h)
    A[i, i] = -2 / h**2 - 2*xi
    A[i, i+1] = 1 / h**2 + xi / (2*h)
    b[i] = 2

# Boundary condition at x = 2.1 for y(2.1) + 0.8y'(2.1) = 1
A[n-1, n-2] = -0.8 / (2*h)
A[n-1, n-1] = 1 + 0.8 / (2*h)
b[n-1] = 1

# Solve the linear system
y = np.linalg.solve(A, b)
print(y)