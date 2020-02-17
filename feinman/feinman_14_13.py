import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from sympy import Function, Eq, Integral, Derivative
from sympy import integrate, simplify, solve, dsolve
from sympy import symbols
from sympy import init_printing, pretty_print

init_printing()

G = symbols('G')
r = symbols('r')
R = symbols('R')
M = symbols('M')


pretty_print('''Approach 1. Gravity potential''')

pretty_print('''
Divide ball into 2 pieces: 
1: inner: [0, r)
2: outer: [r, R]
According to superposition principle gravity potential:\n\n''')

psi_1 = Function('psi_1')(r)
psi_2 = Function('psi_2')(r)
psi = Function('psi')(r)

eq_psi = Eq(psi, psi_1 + psi_2)
pretty_print(eq_psi)

pretty_print('''\nFor inner ball mass is:''')

m = M * r**3 /R**3
pretty_print(m)

pretty_print('\nThen:')
eq_psi = eq_psi.subs(psi_1, - G * m / r)
pretty_print(eq_psi)

pretty_print('''\n For outer:''')
r1 = symbols('r1')
der_m = m.diff(r).subs(r, r1)
pretty_print(Eq(psi_2, Integral( - G * der_m/r1, (r1, r, R))))
p2 = integrate( - G * der_m/r1, (r1, r, R))
p2 = simplify(p2)

eq_psi = eq_psi.subs(psi_2, p2)
pretty_print(simplify(eq_psi))

pretty_print('''Then: ''')
psi = solve(eq_psi, psi)[0]

# assert edge case for r = R
assert psi.subs(r, R) + G * M/R == 0

C = Function('C')(r)
pretty_print(Eq(C, -  Derivative(Function('psi')(r), r)))
eq_C = Eq(C, - psi.diff(r))
pretty_print(eq_C)

C = solve(eq_C, C)[0]

# assert edge case for r = R
assert C.subs(r, R) + G * M/R**2 == 0

# suppose we wave such unis that GM /R **3 = 1, and R = 1
# plot potential `psi` vs distance to the center, r:

rs = np.linspace(0., 1.)
psi = psi.subs({G: 1., M: 1., R: 1.})
f_psi = sym.lambdify(r, psi)
plt.plot(rs, f_psi(rs))

rs = np.linspace(1., 4.)
plt.plot(rs, - 1 / rs)

# field

rs = np.linspace(0., 1.)
C = abs(C.subs({G: 1., M: 1., R: 1.}))
f_C = sym.lambdify(r, C)
plt.plot(rs, f_C(rs))

rs = np.linspace(1., 4.)
plt.plot(rs, 1 / rs ** 2)

plt.show()

pretty_print('''Approach 2. Gravity filed''')

psi = Function('psi')(r)
C = Function('C')(r)
pretty_print(Eq(C, -  Derivative(Function('psi')(r), r)))

diff_eq = Eq(psi.diff(r), G*M/R**3 * r)
pretty_print(diff_eq)

solution = dsolve(diff_eq, psi)
pretty_print(solution)

C1 = solution.subs({
    psi: -G*M/R,
    r: R
})

C1 = solve(C1, symbols('C1'))[0]
pretty_print(simplify(solution.subs('C1', C1)))
