import numpy as np

center = [142,142]
a=50 
b=65

zeros = np.full((281,281),np.nan)
for x in range(0,281):  
    for y in range(0,281):
        if np.sqrt(((x-center[1])**2/a**2 + (y-center[0])**2/b**2))<1:
            zeros[x,y]=1

import matplotlib.pyplot as plt
plt.imshow(zeros)
plt.savefig('test.png')