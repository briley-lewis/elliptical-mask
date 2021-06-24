import numpy as np
import matplotlib.pyplot as plt

def ellipse(x, y, h, k, a, b, A):
    r = (((x - h) * np.cos(A) + (y - k) * np.sin(A)) ** 2 / a ** 2) + (((x - h) * np.sin(A) - (y - k) * np.cos(A)) ** 2 / b ** 2)
    return r

x = np.arange(0,280,1)
y = np.arange(0,280,1)

xv, yv = np.meshgrid(x, y)

r = ellipse(xv, yv, 140, 140, 20, 70, 45)

r[r<=1.0] = 1
r[r>1.0] = 0

plt.imshow(r, origin = 'lower')
plt.savefig('ellipse_test.png')