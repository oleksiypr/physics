from sympy import symbols
from sympy.plotting import plot

x = symbols('x')
k = symbols('k')

p1 = plot(x*x, show=False)
p2 = plot(k*x, show=False)
p1.append(p2[0])


p1.show()