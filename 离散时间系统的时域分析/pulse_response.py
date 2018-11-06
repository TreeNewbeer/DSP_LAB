import matplotlib.pyplot as plt
import numpy as np
import scipy as sy
import control as ctrl
import operator

def stepseq(x, y, z):
    k = list(np.zeros(z - y, dtype = int))
    while x < z:
        k[x-y] = 1
        x += 1
    return k


x = list(map(operator.add, stepseq(0, -5, 50), stepseq(10, -5, 50)))
a = [1, -0.9]
b = [1]

y = sy.signal.convolve(a, x)

print(y)