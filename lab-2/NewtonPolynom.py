from sympy import symbols, expand


def divided_differences(x_values, y_values, k):
    result = 0
    for j in range(k + 1):
        mul = 1
        for i in range(k + 1):
            if i != j:
                mul *= (x_values[j] - x_values[i])
        result += y_values[j] / mul
    return result


def create_newton_polynomial(x_values, y_values):
    div_diff = [divided_differences(x_values, y_values, i) for i in range(1, len(x_values))]

    x = symbols("x")

    def newton_polynomial():
        result = y_values[0]

        for k in range(1, len(y_values)):
            mul = 1
            for j in range(k):
                mul *= (x - x_values[j])
            result += div_diff[k - 1] * mul
        return result

    return expand(newton_polynomial())
