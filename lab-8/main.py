import numpy as np

# параметри задані на початку
h = 0.2
N = 5
x = np.linspace(1.1, 2.1, N+1)

# А - матриця коефіцієнтів СЛАР, b - матриця розв'язків всіх рівнянь СЛАР
A = np.zeros((N+1, N+1))
b = np.zeros(N+1)

# Умова y'(1.1) = 1.5 ] записана апроксимацією y'
A[0, 0] = -1/(2*h)
A[0, 2] = 1/(2*h)
b[0] = 1.5

# Апроксимація всього ДР-2
for i in range(1, N):
    xi = x[i]
    A[i, i-1] = 1/h**2 - xi/(2*h)
    A[i, i] = -2/h**2 - 2*xi
    A[i, i+1] = 1/h**2 + xi/(2*h)
    b[i] = 2

# y(2.1) + 0.8y'(2.1) = 1
A[N, N-2] = -0.8/(2*h)
A[N, N] = 1 + 0.8/(2*h)
b[N] = 1

# Вирішення СЛАР
y = np.linalg.solve(A, b)

# Output the solution
for i in range(N+1):
    print(f"y({round(x[i], 1)}) = {y[i]}")
