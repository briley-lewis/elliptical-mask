import numpy as np
import matplotlib.pyplot as plt



class Ellipse():

    def __init__(self, center, a, b, image_size, theta = 0):
        """ Ellipse class

        Sets parameters for creation of an ellipse.

        Args:
            center (tuple):     center coordinates of the ellipse, origin is (0,0).
            a (float):          semi-major axis
            b (float):          semi-minor axis
            image_size (tuple): size of the array. Must be >= a,b
            theta (float):      Angle to rotate ellipse
        
        Returns:
            None

        """
        
        self.center = center
        self.a = b  # fix major and minor axes, having self.a=a makes it vertical instead of horizontal! 
        self.b = a
        self.theta = theta

        y = np.arange(0,image_size[0],1)
        x = np.arange(0,image_size[1],1) # explain this y dimension first
        self.pixel_array = np.meshgrid(x,y)

    def make_ellipse(self):
        """ make_ellipse

        Creates ellipse on a grid using the equation and the initialization parameters

        Args:
            self (object):  Ellipse object

        Returns:
            None
        
        """

        def ellipse_equation(center, a, b, x, y , theta):
            r = (((x - center[0]) * np.cos(theta) + (y - center[1]) * np.sin(theta)) ** 2 / a ** 2) + ((( x - center[0]) * np.sin(theta) - (y - center[1]) * np.cos(theta)) ** 2 / b ** 2)
            return r


        r_grid = ellipse_equation(self.center, self.a, self.b, self.pixel_array[0], self.pixel_array[1], self.theta)
        r_grid[r_grid<1.0] = 1
        r_grid[r_grid>1.0] = 0

        return r_grid

       
    def apply_elliptical_mask(self, image):

        new_image = self.make_ellipse() * image

        return new_image

test_image = 255 * np.random.rand(300,600)

e = Ellipse((100,100),30, 60, test_image.shape, np.pi/6) #fix center coordinates (maybe backwards?)
masked_image = e.apply_elliptical_mask(test_image)

plt.imshow(masked_image,origin='lower')

plt.colorbar()
#plt.savefig("mask_test.png")
plt.show()


