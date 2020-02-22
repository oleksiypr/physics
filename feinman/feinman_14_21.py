from sympy import Eq
from sympy import init_printing, pretty_print
from sympy import solve, sqrt, simplify
from sympy import symbols

init_printing()

# let ve - orbital speed of Earth
# v0 - initial spaceship speed
# v  -  spaceship speed on 'exit' from Solar system
# Ms, Me - mass of the Sun and Earth resp
# R, r   - Earth orbit radius and Earth radius
ve, v, v0 = symbols('v_e, v v_0')
G, Ms, Me = symbols('G M_s M_e')
R, r = symbols('R, r')

# For the Earth itself
eq_E = Eq(ve**2/2 - G*Ms/R, - G*Ms/R/2)
pretty_print(eq_E)

# For the ship near the Earth
eq_ship = Eq(v0**2/2 - G*Ms/R - G*Me/r, v**2/2)
pretty_print(eq_ship)

res = solve([
    eq_E,
    eq_ship
], v**2, G*Ms/R)

pretty_print(res)

# but for 1st space speed of 11 km/s we have
v1 = symbols('v1')
eq_v1 = Eq(v1**2/2 - G*Me/r, - G*Me/r/2)
pretty_print(eq_v1)

# but for 2dn space speed
v2 = symbols('v2')
eq_v2 = Eq(v2**2/2 - G*Me/r, 0)
pretty_print(Eq(v1**2, solve(eq_v1, v1**2)[0]))
res_sqr_v2 = solve(eq_v2, v2**2)[0]
pretty_print(Eq(v2**2, res_sqr_v2))

res = solve([
    eq_E,
    eq_ship,
    eq_v1
], v0**2, G*Ms/R, G*Me/r)

res_srq_v = res[v0 ** 2]
pretty_print(Eq(v0 ** 2, res_srq_v))
pretty_print('or:')
pretty_print(Eq(v0 ** 2, res_srq_v.subs(v1**2, v2**2/2)))

res_v = sqrt(res_srq_v.subs({
    v1: 11.0,
    ve: 30.0,
    v : 16.0
}))

pretty_print("Relative to Sun  : {0:.2f} km/s".format(res_v))
pretty_print("Relative to Earth: {0:.2f} km/s".format(res_v - 30))




