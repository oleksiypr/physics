from sympy import *
from sympy.vector import CoordSys3D

init_printing()

x, y, z = symbols('x, y, z')

y = x * cos(x)
pretty_print(y)

sqrt()

print(y.subs(x, 3.14))

N = CoordSys3D('N')
v = 2 * N.i + N.j
pretty_print(Eq(sympify('(a**2 + sqrt(b)) / log(x)')))