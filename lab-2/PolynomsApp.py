from LagrangePolynom import *
from NewtonPolynom import *
# range-1
x1_vals = [0, 1, 2, 3]
y1_vals = [1, 3.56, 8.3, 20.23]

# range-2
x2_vals = [0, 1, 1.5, 3]
y2_vals = [1, 3.56, 5.48, 20.23]

print("ІП Лагранжа (1 діапазон):")
print(create_Lagrange_polynomial(x1_vals, y1_vals))
print("ІП Лагранжа (2 діапазон):")
print(create_Lagrange_polynomial(x2_vals, y2_vals))
print("ІП Ньютона (1 діапазон):")
print(create_newton_polynomial(x1_vals, y1_vals))
print("ІП Ньютона (2 діапазон):")
print(create_newton_polynomial(x2_vals, y2_vals))
