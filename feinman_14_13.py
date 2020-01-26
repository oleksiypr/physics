import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, pretty_print
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


def psi(r):
    """
    Gravity potential
    :param r: distance from sphere center, r <= R
    """
    return 1/2 * G * M/R**3 * (r**2 - 3*R**2)


# check psi(R) = - G * M/R
assert ((psi(r).subs(r, R) + G*M/R) == 0)

# Gravity field
C = - psi(r).diff(r)

pretty_print(C)