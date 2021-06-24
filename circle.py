import numpy as np
import matplotlib.pyplot as plt



class Circle():

    def __init__(self, center, r, image_size):
        """ Circle class

        Sets parameters for creation of a circle.

        Args:
            center (tuple):     center coordinates of the ellipse, origin is (0,0).
            r (float):          radius
            image_size (tuple): size of the array. Must be >= r
        
        Returns:
            None

        """
        
        self.center = center
        self.r = r 

        y = np.arange(0,image_size[0],1)
        x = np.arange(0,image_size[1],1) # explain this y dimension first
        self.pixel_array = np.meshgrid(x,y)

    def make_circle(self):
        """ make_circle

        Creates circle on a grid using the equation and the initialization parameters

        Args:
            self (object): Circle object

        Returns:
            None
        
        """

        def circle_equation(center, r, x, y ):
            """ circle_equation

                Describes circle

                Args:
                    center (tuple): center coordinates of the ellipse, origin is (0,0).
                    r (float): radius
                    image_size (tuple): size of the array. Must be >= r

                Returns:
                    type: r_grid
        
                """
            pass ##need to update with equation


        r_grid = circle_equation(self.center, self.r, self.pixel_array[0], self.pixel_array[1])
        r_grid[r_grid<1.0] = 1
        r_grid[r_grid>1.0] = 0

        return r_grid

       
    def apply_circular_mask(self, image):
        """ apply_circular_mask

        Applies mask to an image

        Args:
            self (object):  Circle object
            image (array-like): input image to mask

        Returns:
            array-like: masked image (new_image)
        
        """

        new_image = self.make_circle() * image

        return new_image

test_image = 255 * np.random.rand(300,600)

c = Circle((100,100),30, 60, test_image.shape, np.pi/6) #fix center coordinates (maybe backwards?)
masked_image = c.apply_circular_mask(test_image)

plt.imshow(masked_image,origin='lower')

plt.colorbar()
plt.savefig("mask_test_circ.png")
plt.show()


