import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Ellipse():

    def __init__(self, center, a, b, image_size, theta = 0):
        """ Ellipse class

        Sets parameters for creation of an ellipse.

        Args:
            center (tuple):     center coordinates of the ellipse (y,x), origin is (0,0).
            a (float):          semi-major axis. Must be a > b
            b (float):          semi-minor axis
            image_size (tuple): size of the array (y,x). Must be >= b,a
            theta (float):      angle to rotate ellipse (degrees)
        
        Returns:
            None

        """
        
        self.center = center
        self.a = a
        self.b = b
        
        self.theta = np.deg2rad(theta)

        x = np.arange(0,image_size[1],1)
        y = np.arange(0,image_size[0],1)
        self.pixel_array = np.meshgrid(x,y)

        if a<=b:
            raise ValueError("Invalid input: 'a' must be greater than 'b'")

        if a > image_size[1] or b > image_size[0]:
            raise ValueError("Invalid input: b,a must be >= image_size (y,x)")

    def make_ellipse(self):
        """ make_ellipse

        Creates ellipse on a grid using the equation and the initialization parameters

        Args:
            self (object):  Ellipse object

        Returns:
            array-like: r_grid binary mask with parameters of ellipse with shape 'image_size'
        
        """

        def ellipse_equation(center, a, b, xy , theta):
            """ ellipse_equation

                Describes ellipse

                Args:
                    center (tuple): center coordinates of the ellipse, origin is (0,0).
                    a (float):      semi-major axis
                    b (float):      semi-minor axis
                    x (array-like): 2d numpy array of x coordinates for each pixel in image with shape 'image_size'
                    y (array-like): 2d numpy array of y coordinates for each pixel in image with shape 'image_size'
                    theta (float):  Angle to rotate ellipse (degrees)

                Returns:
                    array-like: r_grid same size as image_size
                
                """
            x = xy[0]
            y = xy[1]
            r = (((x - center[1]) * np.cos(theta) + (y - center[0]) * np.sin(theta)) ** 2 / a ** 2) + ((( x - center[1]) * np.sin(theta) - (y - center[0]) * np.cos(theta)) ** 2 / b ** 2)
            return r


        r_grid = ellipse_equation(self.center, self.a, self.b, self.pixel_array, self.theta)
        r_grid[r_grid<1.0] = 1
        r_grid[r_grid>1.0] = 0

        return r_grid

       
    def apply_elliptical_mask(self, image):
        """ apply_elliptical_mask

        Applies mask to an image

        Args:
            self (object):  Ellipse object
            image (array-like): input image to mask

        Returns:
            array-like: masked image (new_image)
        
        """

        new_image = self.make_ellipse() * image

        return new_image

    
    def png_to_array(self, filename):


        """ 

        Converts PNG file (located in imgmasks directory) into grayscale array passable in apply_elliptical_mask

        Args:
            self (object): Ellipse object
            filename (string): string containing file name (example: "HLTau.png")
        
        Returns:
            bw_image (array): image array in black and white

        """
        
        def rgb2gray(rgb):
            return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

        img=mpimg.imread(filename)
        
        if len(img.shape)==3:
            return rgb2gray(img)

        elif len(img.shape)==2:
            return img
