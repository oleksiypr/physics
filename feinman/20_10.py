import numpy as np
import sympy.physics.units as un
from sympy.functions import *
from sympy.physics.units import Quantity
from utils import *
from sympy.physics.units import convert_to
from sympy import init_printing, pretty_print

init_printing()

# Polar Earth radius
R_P = get_quantity(Quantity("R_P"), un.length, 6356.912 * un.km)

# Equatorial Earth radius
R_E = get_quantity(Quantity("R_E"), un.length, 6378.388 * un.km)

# Average Earth radius
R = (R_P + R_E) / 2

# Now lets play with raw data.
# ND - is a table of normalized raw data.
# All the values are normalized to be integers.
# Where:
#    ND[0] - distances from the center of the Earth, divide by 1000
#    ND[1] - densities at r
#    ND[2] - densities at r + O, if value in this row is 0, then r + O = r = r - O

ND = [[0, 1, 3, 5, 6, 8],
      [3, 4, 5, 7, 8, 8],
      [0, 0, 6, 0, 9, 0]]

# Distances from the center of the Earth:
rs = np.copy(ND[0])
radius_intervals = list(zip(rs, rs[1:]))
assert radius_intervals == [(0, 1), (1, 3), (3, 5), (5, 6), (6, 8)]

# Densities of the Earth
rhos = np.copy(ND[1])
rhos_intervals = [rho2 - rho1 for (rho1, rho2) in zip(rhos, rhos[1:])]
assert rhos_intervals == [1, 1, 2, 1, 0]

for i in range(len(rhos)):
      rho_breach = ND[2][i]
