import sympy.physics.units as un
from sympy import symbols, solve, Eq, pretty_print
from sympy.interactive import init_printing
from sympy.physics.units import Quantity
from sympy.physics.units import convert_to
from utils import *
import numpy as np

init_printing()


E = Quantity("E")
c = Quantity("c")

set_quantity(E, un.energy, 2.15e12 * un.kilo * un.watts * un.hour)
set_quantity(c, un.speed,  3.00e8  * un.m / un.s)
E = convert_to(E, un.joule).n()

print('Heavy water:')
pretty_print(Eq(symbols('D2O'), 2*symbols('D') + symbols('O')))

print('Let nucleosynthesis reaction be like below:')
pretty_print(Eq(symbols('D'), symbols('H_^2')))
pretty_print(Eq(symbols('H^2') + symbols('H^2'), symbols('He_^4')))

print('a).')

m = E/c**2
m = convert_to(m, un.kg).n()

pretty_print("Energy to mass  : {}".format(m))



