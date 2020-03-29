from sympy import Eq, Function, Derivative
from sympy import init_printing, pretty_print
from sympy import solve, simplify
from sympy import symbols

init_printing()

x, rho, pi, r, R, G = symbols('x rho pi r R G')

M     = Function('M')(r)
a_0 = Function('a_0')(x)
a_1 = Function('a_1')(x)
a_2 = Function('a_2')(x)

eq_M = Eq(M,  4 * rho * pi * r**3 / 3)
pretty_print(eq_M)

M0 = eq_M.args[1].subs(r, R)
M2 = eq_M.args[1].subs(r, R/4)

M1 = M0 - M2

eq_a_0 = Eq(a_0, a_1 + a_2)
pretty_print(eq_a_0)

eq_a_0 = eq_a_0.subs({
    a_0: G * M0 / (x + R) ** 2,
    a_2: G * M2 / (x + R + R/4) ** 2
})
pretty_print(eq_a_0)

a_1_solution = simplify(solve(eq_a_0, a_1)[0])
pretty_print(Eq(a_1, a_1_solution))

actual_a1 = G*rho/(x + R)**2 * 4*pi/3*R**3 \
    * (1 - (8 + 2*R/(x + R))**(-2))

assert simplify(a_1_solution - actual_a1) == 0
