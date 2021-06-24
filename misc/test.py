"""playground for trying new things; please ignore"""

def test_fun(x,y):
    """Test function

    Adds x and y and returns their sum. Trying to see if I can write a Napoleon-style docstring.

    Args:
        x (float): any number.
        y (float): any number.

    Returns:
        float: sum """
    return x+y

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
#plt.imshow(zeros)
#plt.savefig('test.png')

import scipy.ndimage
im2 = scipy.ndimage.rotate(zeros,angle=40,order=0,reshape=False)
im2[np.where(np.isnan(im2)==True)] = 0
plt.imshow(im2)
plt.colorbar()
plt.savefig('test2.png')