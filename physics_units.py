from sympy import symbols, solve, Eq, pretty_print
from sympy.physics.units import Quantity, mass, acceleration, power, velocity
from sympy.physics.units import convert_to
from sympy.physics.units import kilo
from sympy.physics.units import km, hour, m, s, kg, W
from sympy.physics.units.systems import SI

a = symbols("a")
m_ = Quantity("m")
v = Quantity("v")
W_ = Quantity("W")

SI.set_quantity_dimension(a, acceleration)

SI.set_quantity_dimension(m_, mass)
SI.set_quantity_scale_factor(m_, 1000*kg)

SI.set_quantity_dimension(v, velocity)
SI.set_quantity_scale_factor(v, 60*km/hour)

SI.set_quantity_dimension(W_, power)
SI.set_quantity_scale_factor(W_, 120*kilo*W)

eq = Eq(W_, m_*a*v)
result = solve(eq, a)[0]
pretty_print(result)

pretty_print(convert_to(result, m / s ** 2).n())


