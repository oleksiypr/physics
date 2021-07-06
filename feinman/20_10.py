from typing import List, Any, Tuple

import numpy as np
import sympy.physics.units as un
from sympy.functions import *
from sympy.physics.units import Quantity
from utils import *
from sympy.physics.units import convert_to
from sympy import init_printing, pretty_print

init_printing()

# Polar Earth radius
R_P_km = 6356.912
R_P = get_quantity(Quantity("R_P"), un.length, R_P_km * un.km)

# Equatorial Earth radius
R_E_km = 6378.388
R_E = get_quantity(Quantity("R_E"), un.length, R_E_km * un.km)

# Average Earth radius
R_km = (6356.912 + 6378.388) / 2
R = get_quantity(Quantity("R"), un.length, R_km * un.km)


# RD - is a table with raw data
# Where:
#    RD[0] - distances from the surface of the Earth, km
#    RD[1] - densities at depth from above row, g/cm^3
#    RD[2] - densities at 'breach', if value is 0, then no 'breach'
RD = [
    [0.0, 30.0, 100.0, 200.0, 400.0, 1000.0, 2000.0, 2900.0, 3500.0, 5000.0, 6000.0],
    [2.6,  3.0,   3.4,   3.5,   3.6,    4.7,    5.2,    5.7,   10.2,   11.5,   17.0],
    [0.0,  3.3,   0.0,   0.0,   0.0,    0.0,    0.0,    9.4,    0.0,   16.8,    0.0]
]

# Now lets play with raw data.
# ND - is a table of normalized raw data.
# All the values are normalized to be integers.
# Where:
#    ND[0] - distances from the center of the Earth multiplied by 1000km, as integer
#    ND[1] - densities at `r` multiplied by 1000g/cm^3, as integer
#    ND[2] - densities at 'breach', if value is 0, then no 'breach', as integer
ND = 1000 * np.array(RD)    # normalize
ND = ND.astype('i')         # as integer
R_km_norm = int(1000 * R_km)

n = len(ND[0])
ND[0] = (R_km_norm * np.ones(n)) - ND[0]

pretty_print(ND)


def radius_intervals_norm(nd):
    rs = nd[0]
    return list(zip(rs, rs[1:]))


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


Test_ND = [[0, 1, 3, 5, 6, 8],
           [3, 4, 5, 7, 8, 8],
           [0, 0, 6, 0, 9, 0]]

assert radius_intervals_norm(Test_ND) == [(0, 1), (1, 3), (3, 5), (5, 6), (6, 8)]
assert rhos_intervals_norm(Test_ND)   == [(3, 4), (4, 5), (6, 7), (7, 8), (9, 8)]

pretty_print(radius_intervals_norm(ND))
pretty_print(rhos_intervals_norm(ND))



