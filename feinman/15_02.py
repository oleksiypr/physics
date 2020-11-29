from sympy import Eq
from sympy import init_printing, pretty_print
from sympy import solve, simplify, sqrt
from sympy import symbols

init_printing()

t1 , t2, t_tau = symbols('t_1 t_2 t_tau', positive=True)
c, u = symbols('c u', positive=True)
L = symbols('L', positive=True)

R = sqrt(1 - u**2/c**2)
L_rel = L * R

eq_t1 = Eq(c*t1, L_rel + u*t1)
eq_t2 = Eq(c*t2, L_rel - u*t2)

pretty_print(eq_t1)
pretty_print(eq_t2)

sol_t1 = solve(eq_t1, t1)[0]
sol_t2 = solve(eq_t2, t2)[0]

pretty_print(Eq(t1, sol_t1))
pretty_print(Eq(t2, sol_t2))

sum_t1_t2 = simplify(sol_t1 + sol_t2)
eq_t_tau = Eq(t_tau, sum_t1_t2)
pretty_print(eq_t_tau)


