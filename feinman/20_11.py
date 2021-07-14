from sympy import *

init_printing()

# //@formatter:off
h   = symbols('h')      # the heights the body stated rolling from
I_0 = symbols('I_0')    # moment of inertia relative (axis) center of gravity
M   = symbols('M')      # the mass
r   = symbols('r', positive=True)      # radius of the body surface in contact with the plane
g   = symbols('g')      # gravity of Earth
# //@formatter:on

print('1). Linear speed of the center of gravity at the end')

# //@formatter:off
omega = symbols('omega')
v     = omega * r
# //@formatter:on

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
v_1 = v.subs(I_0, I_1)
assert v_1 == sqrt(6 * g*h / 5)
pretty_print(Eq(symbols('v_1'), v_1))

print('b) disk')
I_2 = M*r**2 /2
v_2 = v.subs(I_0, I_2)
pretty_print(Eq(symbols('v_2'), v_2))

print('c) disk of mass M_1 and radius R_1 on the shaft with mass m_2 and radius r_2')
M_1, m_2 = symbols('M_1 m_2', positive=True)
R_1, r_2 = symbols('R_1 r_2', positive=True)

I_3 = (M_1 * R_1**2)/2 + (m_2 * r_2**2)/2
v_3 = v.subs({
    I_0: I_3,
    r: R_1,
    M: M_1 + m_2
})

assert simplify(sqrt(2*(M_1 + m_2)*g*h/(3*M_1/2 + m_2*(1 + r_2**2/R_1**2/2))) - v_3) == 0
pretty_print(Eq(symbols('v_3'), simplify(v_3)))
