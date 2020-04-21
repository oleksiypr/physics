from sympy import Eq
from sympy import init_printing, pretty_print
from sympy import solve, simplify, sqrt
from sympy import symbols

init_printing()

x,  t  = symbols('x t')
x_, t_ = symbols('x\' t\'')
u,  c  = symbols('u c')

a = sqrt(1 - u**2/c**2)
b = u/c**2

eq_x = Eq(x_, (x - u*t)/a)
eq_t = Eq(t_, (t - b*x)/a)

pretty_print(eq_x)
pretty_print(eq_t)

res = solve([
    eq_x, eq_t
], x, t)

res_x = res[x]
res_t = res[t]

pretty_print(Eq(x, res_x))
pretty_print(Eq(t, res_t))

_, eq_x_rhs = eq_x.args
_, eq_t_rhs = eq_t.args

assert simplify(eq_x_rhs.subs({
    x: x_, t: t_, u: -u
}) - res_x) == 0

assert simplify(eq_t_rhs.subs({
    x: x_, t: t_, u: -u
}) - res_t) == 0