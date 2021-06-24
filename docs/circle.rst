:orphan:

Circle class
============

Function to generate an elliptical mask and apply it to an image

:class:`imgmasks.circle(self, center, r, image_size)`

Args:
        center (tuple):     center coordinates of the ellipse, origin is (0,0).
        r (float):          radius
        image_size (tuple): size of the array (y,x). Must be >= r
Returns:
        grid of "r" values for each pixel. Pixels with r<1 are inside the circle, and pixels with r>1 are outside the circle.        
=======

