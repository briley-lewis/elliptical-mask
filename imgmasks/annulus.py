import numpy as np
import matplotlib.pyplot as plt


def ellipse_equation(center, a, b, xy , theta):

    theta = np.deg2rad(theta)

    x = xy[0]
    y = xy[1]
    r = (((x - center[1]) * np.cos(theta) + (y - center[0]) * np.sin(theta)) ** 2 / a ** 2) + ((( x - center[1]) * np.sin(theta) - (y - center[0]) * np.cos(theta)) ** 2 / b ** 2)
    return r


test_image = 255 * np.random.rand(300, 600) # random 2-d array of ints

thickness = 20
smaj = 60
smin = 30

x = np.arange(0,test_image.shape[1],1)
y = np.arange(0,test_image.shape[0],1)
pixel_array = np.meshgrid(x,y)

r_grid1 = ellipse_equation((100,150),smaj, smin, pixel_array, 10)
r_grid1[r_grid1<1.0] = 1
r_grid1[r_grid1>1.0] = 0

r_grid2 = ellipse_equation((100,150),smaj+thickness, smin+thickness, pixel_array, 10)
r_grid2[r_grid2<1.0] = 1
r_grid2[r_grid2>1.0] = 0

r_grid  = r_grid2-r_grid1

new_image = r_grid * test_image

plt.imshow(new_image, origin = 'lower')
plt.savefig("annulus_test.png")