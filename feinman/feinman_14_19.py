import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from sympy import symbols, pretty_print, Function, Eq, integrate, simplify, solve, Integral, Derivative, dsolve
from sympy.interactive import init_printing
from sympy.functions import *

init_printing()

print('a).')

a = symbols('a')
b = symbols('b')
e = symbols('e')
pi = symbols('pi')

# let S_o be are of the circle of radius b
# and S is area of ellipse of (a, b) axis
S_o = pi * b**2
k = symbols('k')
S = k * S_o
S = S.subs(k, a/b)
pretty_print(S)

print('\n')
print('b).')

T = symbols('T')
S = S.subs(b, a * sqrt(1 - e**2))
pretty_print(S)

# let sigma = dS/dt
# for ellipse sigma = const by Kepler 2nd law
sigma = symbols('sigma')

# then:
eq_T = Eq(T, S / sigma)
pretty_print(eq_T)

# let v - speed in point B, where point B is a point where
# low axis crossing ellipse:
v = symbols('v')
b = a * sqrt(1 - e**2)

# then for point B:
sigma_eq_B = Eq(sigma, 1/2 * v * b)
pretty_print(sigma_eq_B)

# from  feinman_14_18:
G, M, m = symbols('G, M, m')
E = -1/2 * G * M*m / a
eq_E = Eq(m * v**2 / 2 - G*M*m/a, E)
pretty_print(eq_E)

# then:

T, _, _ = solve([
    sigma_eq_B,
    eq_E,
    eq_T
], T, sigma, v)[1]

pretty_print(T**2)
print('\n')

print('c).')
epsilon = symbols('epsilon')
epsilon_eq = Eq(epsilon, E/m)
pretty_print(epsilon_eq)
a = solve(epsilon_eq, a)[0]
pretty_print(a)

pretty_print((T**2).subs('a', a))

