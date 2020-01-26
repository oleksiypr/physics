import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, pretty_print, Function, Eq, integrate, simplify, solve
from sympy.interactive import init_printing

init_printing()

"""
x = np.arange(1., 2., 0.01)
plt.plot(x, 2 - x)

x = np.arange(0., 1., 0.01)
plt.plot(x, x ** 2)
plt.show()
"""

G = symbols('G')
r = symbols('r')
R = symbols('R')
M = symbols('M')


# Approach 1. Gravity potential.
'''
Divide ball into 2 pieces: 
- inner: [0, r)
- outer: [r, R]
'''

psi_1 = Function('psi_1')(r)
psi_2 = Function('psi_2')(r)
psi = Function('psi')(r)

eqP = Eq(psi, psi_1 + psi_2)
pretty_print(eqP)

m = M * r**3 /R**3
eqP = eqP.subs(psi_1, - G * m / r)
pretty_print(eqP)

r1 = symbols('r1')
der_m = m.diff(r).subs(r, r1)
p2 = integrate( - G * der_m/r1, (r1, r, R))
p2 = simplify(p2)

eqP = eqP.subs(psi_2, p2)
pretty_print(simplify(eqP))

psi = solve(eqP, psi)[0]

# assert edge case for r = R
assert psi.subs(r, R) + G * M/R == 0

C = Function('C')(r)
eqC = Eq(C, - psi.diff(r))
pretty_print(eqC)

C = solve(eqC, C)[0]

# assert edge case for r = R
assert C.subs(r, R) + G * M/R**2 == 0

# suppose we wave such unis that GM /R **3 = 1, and R = 1

# potential

rs = np.linspace(0., 1.)
psi = psi.subs({G: 1., M: 1., R: 1.})
psi = [psi.subs(r, r1) for r1 in rs]

plt.plot(rs, psi)

rs = np.linspace(1., 4.)
plt.plot(rs, - 1 / rs)

# field

rs = np.linspace(0., 1.)
C = abs(C.subs({G: 1., M: 1., R: 1.}))
C = [C.subs(r, r1) for r1 in rs]

plt.plot(rs, C)

rs = np.linspace(1., 4.)
plt.plot(rs, 1 / rs ** 2)

plt.show()
