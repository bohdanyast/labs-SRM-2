from sympy import symbols, expand


def create_basic_polynomial(x_values, i):
    x = symbols("x")

    divider = 1
    result = 1
    for j in range(len(x_values)):
        if j != i:
            result *= (x - x_values[j])
            divider *= (x_values[i] - x_values[j])
    return result / divider


def create_Lagrange_polynomial(x_values, y_values):
    basic_polynomials = [create_basic_polynomial(x_values, i) for i in range(len(x_values))]
    lagrange_polynomial = sum((y_values[i] * basic_polynomials[i] for i in range(len(y_values))))

    return expand(lagrange_polynomial)
