from sympy import symbols, pretty_print, Eq, simplify
from sympy.interactive import init_printing

init_printing()

F, k, x = symbols('F k x')
f, u = symbols('f u')

eq_1 = Eq(F, - k*x)
pretty_print(eq_1)

eq_2 = eq_1.subs(F, F + f).subs(x, x + u)
pretty_print(eq_2)

lhs_1, rhs_1 = eq_1.args
lhs_2, rhs_2 = eq_2.args

pretty_print(simplify(Eq(lhs_2 - lhs_1, rhs_2 - rhs_1)))
