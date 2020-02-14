from sympy import symbols, pretty_print, Eq, solve
from sympy.functions import *
from sympy.interactive import init_printing

init_printing()

E = symbols('E')
e = symbols('e')
a = symbols('a')
v = symbols('v')
v_a = symbols('v_a')
m = symbols('m')
M = symbols('M')
G = symbols('G')

E_eq_1 = Eq(E, m * v ** 2 / 2 - G * M*m / a)
E_eq_2 = Eq(E, m * v_a**2 / 2 - G * M*m / (a*(1 + e)))

pretty_print(E_eq_1)
pretty_print(E_eq_2)

eq_kepler_law_2 = Eq(v*a*sqrt(1 - e**2), v_a * a*(1 + e))

pretty_print(eq_kepler_law_2)

res_E, _, _ = solve([
    E_eq_1,
    E_eq_2,
    eq_kepler_law_2
], E, v, v_a)[0]

pretty_print(res_E)