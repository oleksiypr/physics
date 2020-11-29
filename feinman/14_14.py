from sympy import pretty_print, Eq, solve, symbols
from sympy.interactive import init_printing

init_printing()

g = 9.8
P = 0.025 * g
k = 15.3
m = 0.050
h = 0.09

delta_x = symbols('delta_x')
eq = Eq(m**2 / (P + m*g) * g*h, - m*delta_x + k/(2*g) * delta_x**2)
pretty_print(eq)
solution = solve(eq, delta_x)
pretty_print(solution)

delta_x = solution[1]
result = h + delta_x
print("result is {0:.1f} cm".format(result * 100))
