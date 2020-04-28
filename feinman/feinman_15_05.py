import numpy as np
from sympy.interactive import init_printing

init_printing()

w = 1.4 # kW/m^2
c = 3e8 # m/s

M_He4 = 4.0039 # gram/mol
M_H   = 1.0080 # gram/mol

dM = 4 * M_H - M_He4 # gram/mol
print('dM = {0:.4f} gram/mol'.format(dM))

# distance Sun-Earth
R = 1.5e11               # meters
W = 4 * np.pi * R**2 * w # kW
q = W/c**2               # tonnes/s
print('q = {:e} tonnes'.format(q))

q_H = 4 * q * M_H / dM # tonnes/s
print('result: {:e} tonnes/s'.format(q_H))
