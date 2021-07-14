from sympy import *

init_printing()

# //@formatter:off
h   = symbols('h')      # the heights the body stated rolling from
I_0 = symbols('I_0')    # moment of inertia relative (axis) center of gravity
M   = symbols('M')      # the mass
r   = symbols('r')      # radius of the body surface in contact with the plane
g   = symbols('g')      # gravity of Earth
# //@formatter:on

print('1). Linear speed of the center of gravity at the end')

omega = symbols('omega')
v     = omega * r

eq_energy_conservation = Eq(
    M*g*h,
    M * v**2 /2 + I_0 * omega**2 /2
)
pretty_print(eq_energy_conservation)

# //@formatter:off
omega = solve(eq_energy_conservation, omega)[1]
v     = omega * r
# //@formatter:on
pretty_print(Eq(symbols('v'), v))

print('2). Apply above for cases:')
print('a) sphere')

I_1 = 2 * M*r**2 / 3  # sphere
v_1 = simplify(v.subs(I_0, I_1))
pretty_print(Eq(symbols('v_1'), v_1))



