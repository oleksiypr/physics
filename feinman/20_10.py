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


def radius_intervals_norm(nd):
    rs = nd[0]
    return list(zip(rs, rs[1:]))


assert radius_intervals_norm(ND) == [(0, 1), (1, 3), (3, 5), (5, 6), (6, 8)]


def rhos_intervals_norm(nd):
    # Densities of the Earth
    rhos = nd[1]
    intervals = list(zip(rhos, rhos[1:]))

    # Correct densities intervals with 'breach' values if a preach present
    for i in range(len(intervals)):
        rho_breach = nd[2][i]
        _, end = intervals[i]
        if rho_breach != 0:
            intervals[i] = (rho_breach, end)

    return intervals


assert rhos_intervals_norm(ND) == [(3, 4), (4, 5), (6, 7), (7, 8), (9, 8)]


radius_intervals = [(r1  /1000.0, r2  /1000.0) for (r1  , r2)   in radius_intervals_norm(ND)]
rhos_intervals   = [(rho1/1000.0, rho2/1000.0) for (rho1, rho2) in rhos_intervals_norm(ND)]

pretty_print(radius_intervals)
pretty_print(rhos_intervals)
