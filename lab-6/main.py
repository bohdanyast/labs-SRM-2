import gauss_method as gm
import seidel_method as sm
import simple_iterations_method as sim

gauss_matrix = [
    [9, -5, -6, 3],
    [1, -7, 1, 0],
    [3, -4, 9, 0],
    [6, -1, 9, 8],
]

gauss_solves = [-8, 38, 47, -8]

print("Вирішення СЛАР методом Гауса:")
print(gm.solve_by_gauss_method(gauss_matrix, gauss_solves))
print("Визначник, обчислений методом Гауса:")
print(gm.get_determinant(gauss_matrix, gauss_solves))
print("Обернена матриця:")
print(gm.get_reversed_matrix(gauss_matrix))

print()

sim_sm_matrix = [
    [16, -8, 0, 0, 0],
    [-7, -16, 5, 0, 0],
    [0, 4, 12, 3, 0],
    [0, 0, -4, 12, -7],
    [0, 0, 0, -1, 7]
]

sim_sm_solves = [0, -123, -68, 104, 20]

print("Вирішення СЛАР методом Зейделя:")
print(sm.seidel_method(sim_sm_matrix, sim_sm_solves, 0.01))

print()

print("Вирішення СЛАР методом простих ітерацій:")
print(sim.iterative_method(sim_sm_matrix, sim_sm_solves, 0.01))

