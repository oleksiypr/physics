import sympy.physics.units as un
from sympy import symbols, Eq, pretty_print
from sympy.interactive import init_printing
from sympy.physics.units import Quantity
from sympy.physics.units import convert_to
from utils import *

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
m = symbols('m')
pretty_print(Eq(m, symbols('E')/c**2))
m = E/c**2
m = convert_to(m, un.kg).n()

pretty_print("Energy to mass  : {}".format(m))

print('b).')
M_D   = Quantity('M_D')
M_He4 = Quantity('M_He4')
M_O   = Quantity('M_O')

set_quantity(M_D,   un.mass/un.amount_of_substance,  2.0147 * un.gram / un.mol)
set_quantity(M_He4, un.mass/un.amount_of_substance,  4.0039 * un.gram / un.mol)
set_quantity(M_O,   un.mass/un.amount_of_substance, 15.9990 * un.gram / un.mol)

dM = 2 * M_D - M_He4
dM = convert_to(dM, un.gram / un.mol).n()
print('dM = {}'.format(dM))

v_He = m / dM
v_He = convert_to(v_He, un.mol).n()

v_D2O = v_He
print('v_D2O = {}'.format(v_D2O))
M_D20 = 2*M_D + M_O
M_D20 = convert_to(M_D20, un.gram / un.mol)
print('M_D20 = {}'.format(M_D20))

m_D20 = M_D20 * v_D2O
m_D20 = convert_to(m_D20, un.kg)
print('Mass of heavy water for nucleosynthesis reaction for a year: {}'.format(m_D20))

m_D20_per_second = m_D20/365/24/3600
m_D20_per_second = convert_to(m_D20_per_second, un.grams)
print('Mass of heavy water for nucleosynthesis reaction per second: {}'.format(m_D20_per_second))



