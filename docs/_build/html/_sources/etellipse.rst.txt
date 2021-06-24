:orphan:

Ellipse
=======

Function to generate an elliptical mask and apply it to an image

:class:`imgmasks.ellipse(center, a, b, image_size, theta=0)`

Args:
        center (tuple):     center coordinates of the ellipse, origin is (0,0).
        a (float):          semi-major axis
        b (float):          semi-minor axis
        image_size (tuple): size of the array. Must be >= a,b
        theta (float):      Angle to rotate ellipse
Returns:
        grid of "r" values for each pixel. Pixels with r<1 are inside the ellipse, and pixels with r>1 are outside the ellipse.        
