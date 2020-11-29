import numpy as np

c = 3.0e8   # m/s
v = 0.99    # c
S = 5.0     # km
R = np.sqrt(1 - v**2)

# a)

t = S * 1000. /(v * c)
print("a). t = {0:.3} us".format(t * 1e6))

# b)

S_ = S * R
print("b). S' = {0:.4} m".format(S_ * 1000))
