from sympy import symbols, solve, Eq, pretty_print, sympify, expand
from sympy.functions import *

s1 = symbols("s1")
s2 = symbols("s2")
s = symbols("s")
h = symbols("h")
g = symbols("g")
v = symbols("v")
m = symbols("m")
t = symbols("t")
delta_h = symbols("Delta_h")

A = m*v**2/2

res_v = solve([
        Eq(s1, v*sqrt(2)*t),
        Eq(v*sqrt(2), 2*g*t),
        Eq(delta_h, g * t**2 / 2),
        Eq((v *sqrt(2)/2)**2, 2 * g * delta_h)
    ], v, t, delta_h)[1]

A = A.subs({"v": res_v[0]})

res_s2 = solve([
    Eq(s2, v*sqrt(2)/2 * t),
    Eq(h, v*sqrt(2)/2 * t + g * t**2 / 2),
    Eq(s, s1 + s2),
    Eq(v**2, res_v[0]**2)
], s2, s1, t, v)


s1 = res_s2[1][1]
A = A.subs({"s1": s1})
pretty_print(A)

n = 3
distances = [19.4 , 60.0 , 86.1]
masses    = [ 7.26,  2.00, 0.81]

for i in range(n):
    print(A.subs({g: 9.81, m: masses[i], s: distances[i], h: 1.8}))
