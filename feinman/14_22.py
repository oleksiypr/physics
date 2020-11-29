from sympy import Eq
from sympy import init_printing, pretty_print
from sympy import solve, sqrt
from sympy import symbols

init_printing()

# Here I changed initial condition to rid off 16 km/s "on exit".
# In another words 0 "on exit" where "exit" is far far away aka 'oo'.
# As per 14.21:
ve, v, v0 = symbols('v_e v v_0')
v1, v2 = symbols('v1 v2')
G, Ms, Me = symbols('G M_s M_e')
R, r = symbols('R, r')

eq_sqr_ve = Eq(ve ** 2,     G*Ms / R)
eq_sqr_v1 = Eq(v1 ** 2,     G*Me / r)
eq_sqr_v2 = Eq(v2 ** 2, 2 * G*Me / r)
pretty_print(eq_sqr_ve)
pretty_print(eq_sqr_v1)
pretty_print(eq_sqr_v2)

# For the ship near the Earth and on "exit" far far away:
eq_ship = Eq(v0**2/2 - G*Ms/R - G*Me/r, 0)
pretty_print(eq_ship)

solution1 = solve([
    eq_sqr_ve,
    eq_sqr_v1,
    eq_ship
], v0**2, G*Ms/R, G*Me/r)

pretty_print(Eq(v0**2, solution1[v0**2]))

print('or:')

solution2 = solve([
    eq_sqr_ve,
    eq_sqr_v2,
    eq_ship
], v0**2, G*Ms/R, G*Me/r)

pretty_print(Eq(v0**2, solution2[v0**2]))

rev_v0 = sqrt(solution1[v0**2].subs({v1: 11.0, ve: 30.0}))
pretty_print('Relative to Sun  : {0:.2f} km/s'.format(rev_v0 + 30.0))

# As per 14.21 with 16km/s on exit:
pretty_print('As per 14.21 with 16km/s on exit: {0:.2f} km/s'.format(47.9 + 30))
pretty_print('Not too much difference')
