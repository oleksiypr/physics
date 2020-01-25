from sympy import symbols, solve, Eq, pretty_print
from sympy.physics.units import Quantity
import sympy.physics.units as un
from sympy.physics.units import convert_to
from sympy.physics.units.systems import SI
from sympy.functions import *
from sympy.physics.units.definitions.unit_definitions import One
from sympy.interactive import init_printing
from utils import *

init_printing()

hp_to_watts = 745.7

W0 = Quantity("W0")
W = Quantity("W")
m = Quantity("m")
v = Quantity("v")
g = Quantity("g")
theta = symbols("theta")

set_quantity(W0, un.power,         85 * hp_to_watts * un.watts)
set_quantity(W,  un.power,         20 * hp_to_watts * un.watts)
set_quantity(m,  un.mass,        1200 * un.kg)
set_quantity(v,  un.velocity,      48 * un.km / un.hour)
set_quantity(g,  un.acceleration,   9.81 * un.m / un.s ** 2)

eq = Eq(sin(theta), (W0 - W) / (m*g*v))
pretty_print(eq)

theta = solve(eq, theta)[1]

theta = convert_to(theta, un.watts).n()
pretty_print(convert_to(theta, un.degrees).n())
