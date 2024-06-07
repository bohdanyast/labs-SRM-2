from sympy import *
import matplotlib.pyplot as plt


def find(points, x):
    return_S = None
    S_check_minus = None
    S_check_plus = None
    return_i = None

    h = {}
    for i in range(1, len(points)):
        h[i] = points[i][0] - points[i - 1][0]

    q = {}
    for i in range(len(points)):
        q[i] = symbols(f"q{i}")

    q[0] = 0
    q[len(points) - 1] = 0

    for i in range(1, len(points) - 1):
        q[i] = S(S(points[i + 1][1] - points[i][1]) / S(h[i + 1]) - S(points[i][1] - points[i - 1][1]) / S(h[i]) - S(
            q[i - 1] * h[i]) / S(6) - S(q[i + 1] * h[i + 1]) / S(6)) / S((h[i] + h[i + 1]) * Rational(1, 3))
        solvedd = solve(q[i], symbols(f"q{i}"))

        if len(solvedd) == 1:
            q[i] = solvedd[0]

    for i in range(1, len(points) - 1):
        for jj in range(len(points)):
            for j in range(len(points)):
                q[i] = q[i].subs(symbols(f"q{j}"), q[j])

    x = symbols("x")
    for i in range(1, len(points)):
        # if x >= points[i-1][0] and x <= points[i][0]:
        return_S = q[i - 1] * S((points[i][0] - x) ** 3) / S(6 * h[i]) + q[i] * S((x - points[i - 1][0]) ** 3) / S(
            6 * h[i]) + (Rational(points[i - 1][1], h[i]) - q[i - 1] * Rational(h[i], 6)) * (points[i][0] - x) + (
                               Rational(points[i][1], h[i]) - q[i] * Rational(h[i], 6)) * (x - points[i - 1][0])

        S_check_minus = q[i - 1] * Rational(h[i], 6) + q[i] * Rational(h[i], 3) + Rational(points[i][1] - points[i - 1][1], h[i])

        if i < len(points) - 1:
            S_check_plus = -q[i] * Rational(h[i + 1], 3) - q[i + 1] * Rational(h[i + 1], 6) + Rational(
points[i + 1][1] - points[i][1], h[i + 1])

        return_i = i

    return return_S, S_check_minus, S_check_plus, return_i


inputting = ((-0.1, 1.9823), (0.2, 1.6710), (0.5, 1.3694), (0.8, 1.0472), (1.1, 0.64350))
input_x = 1

print(f"Input = {inputting}")
print(f"X* = {input_x}")
found_S, S_check_minus, S_check_plus, i = find(inputting, input_x)

if S_check_minus == None or S_check_plus == None:
    print("Unable to check correctness of the algorithm!")
else:
    if N(S_check_minus.subs(symbols("x"), input_x)) == N(S_check_plus.subs(symbols("x"), input_x)):
        print("The algorithm works correctly.")
    else:
        print("The algorithm seems to not be working correctly..")
print(f"S({input_x})_{i} = {N(found_S.subs(symbols('x'), input_x))}")

x = [point[0] for point in inputting]
y = [point[1] for point in inputting]
plt.scatter(x, y, color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot of the data')
plt.grid(True)
plt.legend()

sympy_plot = plot(found_S, show=False)

# Convert the SymPy plot to a Matplotlib plot and overlay it onto the existing plot
for line in sympy_plot:
    xdata, ydata = line.get_points()
    plt.plot(xdata, ydata, label='Function f(x)')

plt.show()
