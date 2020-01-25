import sympy.physics.units as un
from sympy import symbols, solve, Eq, pretty_print
from sympy.physics.units import Quantity
from sympy.physics.units import convert_to
from sympy.physics.units import length, acceleration, mass
from sympy.physics.units.definitions.unit_definitions import One
from sympy.physics.units.systems import SI
from sympy.interactive import init_printing

init_printing()

Wo = symbols("Wo")
v = symbols("v")

rho = Quantity("rho")
s = Quantity("s")
g = Quantity("g")
h1 = Quantity("h1")
h2 = Quantity("h2")
etha = Quantity("etha")
theta = Quantity("theta")

SI.set_quantity_dimension(rho, mass / length ** 3)
SI.set_quantity_scale_factor(rho, 1.0 * un.grams / un.cm ** 3)

SI.set_quantity_dimension(s, length**2)
SI.set_quantity_scale_factor(s, 35.0 * un.cm**2)

SI.set_quantity_dimension(h1, length)
SI.set_quantity_scale_factor(h1, 2.4 * un.meters)

SI.set_quantity_dimension(h2, length)
SI.set_quantity_scale_factor(h2, 4.8 * un.meters)

SI.set_quantity_dimension(g, acceleration)
SI.set_quantity_scale_factor(g, 9.81 * un.m/un.s**2)

SI.set_quantity_dimension(etha, One)
SI.set_quantity_scale_factor(etha, 0.6)

SI.set_quantity_dimension(theta, One)
SI.set_quantity_scale_factor(theta, 30 * un.degrees)

eq1 = Eq(etha*Wo, rho*s*v*g*h1 + rho*s*v* v**2/2)
eq2 = Eq(v ** 2, 8*g*h2)
# eq2 = Eq((v * sin(theta))**2, 2*g*h2)

pretty_print(eq1)
pretty_print(eq2)

res = solve((eq1, eq2), (v, Wo))[1][1]

pretty_print(res)
pretty_print(convert_to(res, un.watts).n())







