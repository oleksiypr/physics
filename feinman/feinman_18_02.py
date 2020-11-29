import numpy as np
from sympy.interactive import init_printing

init_printing()

R     = 6371000         # m
day   = 24*3600         # sec
omega = 2*np.pi / day   # rad/sec

delta_v = - 200.0   # m/s
lat_LA  =    34.05  # degrees


def v(phi):
    return omega * R * np.cos(np.radians(phi))


v_LA = v(lat_LA)
v    = v_LA + delta_v

print('Los Angeles velocity : {0:.2f} m/s'.format(v_LA))
print('Target point velocity: {0:.2f} m/s'.format(v))

lat = np.rad2deg(np.arccos(v / (omega*R)))

print('Target point latitude: {0:.2f} degrees'.format(lat))