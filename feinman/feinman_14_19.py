import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from sympy import symbols, pretty_print, Function, Eq, integrate, simplify, solve, Integral, Derivative, dsolve
from sympy.interactive import init_printing

init_printing()

# a)

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