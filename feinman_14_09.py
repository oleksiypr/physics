from sympy import symbols, solve, Eq, pretty_print

M = symbols("M")
L = symbols("L")
g = symbols("g")
v = symbols("v")

U1 = - (M*L) * g * L/4
U2 = - (M*L) * g * L/2

dU = U2 - U1

eq = Eq(-dU, (M*L) * v**2 / 2)

solution = solve(eq, v)[0]
pretty_print(solution)
