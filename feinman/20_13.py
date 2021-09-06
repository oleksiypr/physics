from sympy import *
import numpy as np

init_printing()

# //@formatter:off
h       = 61.                 # meters, the sea level increase after ice got melted
phi_ice = 80.                 # degrees, an average latitude of the ice
phi_ice = np.radians(phi_ice) # radians, an average latitude of the ice

R     = 6370.  # kilometers, the Earth radius
rho_w = 1000.  # kg/m^3, density of the water

omega_0 = 2 * np.pi / 24    # rad/hour, the Earth rotation
omega_0 =   omega_0 / 3600  # rad/sec, the Earth rotation

I0 = 8.11e37    # kg*m^2, the Earth moment of inertia
# //@formatter:on

# The equation of the Earth rotation change after the ice got melted:
pretty_print(
    Eq(
        symbols('delta_omega')/symbols('omega_0'),
        - symbols('m')*symbols('R')**2/(15*symbols('I_0')) * (6 - 5*cos(symbols('phi_ice'))**2)
   )
)

# convert R to meters
R = R * 1000

# mass of the ice
m = 4 * np.pi * rho_w * R**2 * h

# a change of the Earth rotation, rad/sec:
delta_omega = - omega_0 * m*R**2 * (6 - 5*np.cos(phi_ice)**2) / (15*I0)


# a change of the Earth rotation period, seconds:
delta_T = - 2*np.pi / omega_0**2 * delta_omega

print('A change of the Earth rotation period, seconds: {0:.3f} sec'.format(delta_T))

