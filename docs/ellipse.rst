:orphan:

Ellipse
=======

Module for generating an elliptical mask and applying it to an image.

:class:`imgmasks.ellipse(center, a, b, image_size, theta=0)`

Sets parameters for creation of an ellipse

**Parameters**:
        
        **center** (tuple):     center coordinates of the ellipse, origin is (0,0).
        
        **a** (float):          semi-major axis
        
        **b** (float):          semi-minor axis
        
        **image_size** (tuple): size of the array. Must be >= a,b
        
        **theta** (float):      Angle to rotate ellipse

**Returns**:
        None

:class:`imgmasks.ellipse.make_ellipse(self)`

Creates ellipse on a grid using the equation and initialization parameters

**Args**:
        **self** (object):      Ellipse object

**Returns**:
        
        **r_grid** (array):     array of "r" values for each pixel: pixels with r<1 are inside the ellipse, and pixels with r>1 are outside the ellipse. 



:class:`imgmasks.ellipse.apply_elliptical_mask(image)`

Applies mask to an image

**Args**:
        
        **self** (object):      Ellipse object
        
        **image** (array):      input image to mask

**Returns**:
        **new_image** (array):  masked image


