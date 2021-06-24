#end to end test of ellipse mask
from imgmasks import circle 
import numpy as np
import matplotlib.pyplot as plt



def test_make_circle():

    test_image = 255 * np.random.rand(300, 600) # random 2-d array of ints

    c = circle.Circle((100,100), 30, test_image.shape) #fix center coordinates (maybe backwards?)

    vals = np.unique(c.make_circle())
    assert len(vals) == 2
    assert vals[0] == 0
    assert vals[1] == 1

def test_apply_elliptical_mask():

    test_image = 255 * np.random.rand(300,600) 

    c = circle.Circle((100,100),30, test_image.shape) 
    c_array = c.make_circle() #can't think of a better name for this
    masked_image = c.apply_circular_mask(test_image)
     
    unmasked, masked = np.where(c_array == 1), np.where(c_array == 0)
    assert masked_image[masked].all() == 0
    assert test_image[unmasked].all() == masked_image[unmasked].all()



