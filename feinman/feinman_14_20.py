from sympy import Eq
from sympy import init_printing, pretty_print
from sympy import solve, sqrt
from sympy import symbols

init_printing()

# let v1 - 1st space speed, R - radius of the Earth
# v0 - start speed
# v - speed of the ship on the distance r from the Earth
v1, R = symbols('v_1 R', positive=True)
v0, v, r = symbols('v_0 v r', positive=True)
M, m = symbols('M m', positive=True)
G = symbols('G')

eq_1 = Eq(m * v1**2 /2 - G * M*m /R, 0)
eq_2 = Eq(m * v0**2 /2 - G * M*m /R, m * v**2 /2 - G * M*m /r)

pretty_print(eq_1)
pretty_print(eq_2)

k = symbols('k')
eq_1 = eq_1.subs(G*M*m, k)
eq_2 = eq_2.subs(G*M*m, k)

pretty_print(eq_1)
pretty_print(eq_2)

solution = solve([eq_1, eq_2], v**2, k)[v**2]
pretty_print(Eq(v**2, solution))

res = sqrt(solution.subs({
    r: 1e6,
    R: 6378.0,
    v1: 11.0,
    v0: 12.0
}))
pretty_print("{0:.2f} km/s".format(res))
