import numpy as np
from sympy import init_printing, pretty_print

init_printing()

g = 9.8     # m/s**2
M = 4.0     # kg
h = 0.215   # cm
omega = 120 # rpm
omega = 2 * np.pi * omega / 60  # rad/sec

m = g*M / (h * omega**2 - g)

pretty_print("m = {0:.2f} kg".format(m))