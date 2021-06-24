import numpy as np
import matplotlib.pyplot as plt



class Circle():

    def __init__(self, center, r, image_size):
        """ Circle class

        Sets parameters for creation of a circle.

        Args:
            center (tuple):     center coordinates of the ellipse, origin is (0,0).
            r (float):          radius
            image_size (tuple): size of the array (y,x). Must be >= r 
        
        Returns:
            None

        """
        
        self.center = center
        self.r = r 

        y = np.arange(0,image_size[0],1)
        x = np.arange(0,image_size[1],1) # explain this y dimension first
        self.pixel_array = np.meshgrid(x,y)

        if image_size[0]<r or image_size[1]<r:
            raise ValueError('Image size must be greater than or equal to radius')

    def make_circle(self):
        """ make_circle

        Creates circle on a grid using the equation and the initialization parameters

        Args:
            self (object): Circle object

        Returns:
            None
        
        """

        def circle_equation(center, r, xy):
            """ circle_equation

                Describes circle

                Args:
                    center (tuple): center coordinates of the ellipse, origin is (0,0).
                    r (float): radius
                    x (array-like): 2d array of x coordinates
                    y (array-like): 2d array of y coordinates

                Returns:
                    array-like: r_norm, same size as image size
        
                """
            x = xy[0] ##breaks pixel array up into x and y
            y = xy[1]
            r_norm = ((x-center[1])**2 + (y-center[0])**2)/(r**2)
            return r_norm


        r_grid = circle_equation(self.center, self.r, self.pixel_array)
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
            array-like: masked image same size as input image (new_image)
        
        """

        new_image = self.make_circle() * image

        return new_image



