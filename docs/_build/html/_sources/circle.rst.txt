:orphan:

Circle class
============

Function to generate an elliptical mask and apply it to an image

:class:`imgmasks.circle(self, center, r, image_size)`

**Parameters**:
        
        **center** (tuple):     center coordinates of the circle, origin is (0,0).
        
        **r** (float):          radius
        
        **image_size** (tuple): size of the array. Must be >= r

**Returns**:
        None

:class:`imgmasks.circle.make_circle(self)`

Creates circle on a grid using the equation and initialization parameters

**Args**:
        **self** (object):      Circle object

**Returns**:
        
        **r_grid** (array):     array of "r" values for each pixel: pixels with r<1 are inside the circle, and pixels with r>1 are outside the circle. 



:class:`imgmasks.circle.apply_circular_mask(image)`

Applies mask to an image

**Args**:
        
        **self** (object):      Circle object
        
        **image** (array):      input image to mask

**Returns**:
        **new_image** (array):  masked image
        


