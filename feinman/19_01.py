from sympy import *

init_printing()

M, L = symbols('M L')
omega_0, omega_1 = symbols('omega_0 omega_1')

b = M*L**2
B = b.subs({M: 2*M, L: 2*L})

I_k = 40/3*b
I_B_G = B / 12

I_B_0 = I_B_G + (2*M)*(L**2)
I_B_1 = I_B_G

I_0 = I_k + 4*I_B_0
I_1 = I_k + 4*I_B_1

eq_omega = Eq(I_0*omega_0, I_1*omega_1)
pretty_print(eq_omega)

solution_omega = solve(eq_omega, omega_1)
pretty_print(Eq(omega_1, solution_omega[0]))

omega_1 = solution_omega[0]

A = I_1 * omega_1**2 / 2 - I_0 * omega_0**2 / 2
pretty_print(Eq(symbols('A'), A))