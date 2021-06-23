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
        self.a = a
        self.b = b
        self.ellipse = np.zeros(image_size)
        self.theta = theta

    def make_ellipse(self):
        """ make_ellipse

        Creates ellipse on a grid using the equation and the initialization parameters

        Args:
            self (object):  Ellipse object

        Returns:
            None
        
        """



    

class Mask(Ellipse):

    def __init__(self, center, a, b, image_size, theta = 0):
        """ Mask

        Set parameters for Elliptical Mask.

        Args:
            Ellipse (object): Parent object. Takes in center, a,b, image_size, theta

        Returns:
            None

        """
        super().__init__(center, a, b, image_size, theta = 0)
        self.mask = np.zeros(image_size)


    def make_elliptical_mask(self):
        """ make_elliptical_mask

        Creates a binary elliptical mask, where values are 1 inside and 0 outside the ellipse
        
        Args: 
            None

        Returns:
            None

        """

        
        self.make_ellipse()
        #set self.mask equal to 1 inside and 0 outside of self.ellipse
        
       
    def apply_elliptical_mask(self, image):

        self.make_elliptical_mask()

        new_image = self.mask * image

    def __add__(self, other):

        """__add__

        This may/may not be useful, just thought it was cool. Overrides the add function so that you can
        combine masks using 'Mask 1 + Mask 2'. Curently returns an array, should probably return a Mask object
        so that you can use 'apply_elliptical_mask'

        Args:
            self (Mask object): Initial Mask object
            other (Mask object):Other Mask object

        Returns: 
            2-d array
        
        """

        if self.mask.shape == other.mask.shape:
            
            new_mask = self.mask + other.mask
            rows, cols = np.where(new_mask > 1)
            new_mask[rows, cols] = 1

            return new_mask

        else:

            raise Exception("Mask arrays must be same size!")




