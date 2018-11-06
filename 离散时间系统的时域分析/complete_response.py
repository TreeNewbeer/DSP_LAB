import matplotlib.pyplot as plt
import numpy as np

y = [0, 1]


def Counter(x = []):
    i = 2
    while i < 20:
        x.append((5/6) * x[i-1] - (1/6) * x[i-2] + np.cos(i*np.pi/4) / 6)
        i += 1              
Counter(y)       
x = np.arange(0, 20, 1)
#print(len(y))
#print(len(x))
plt.plot(x, y)
plt.show()