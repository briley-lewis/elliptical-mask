#end to end test of ellipse mask
from imgmasks import ellipse
import numpy as np
import matplotlib.pyplot as plt


def test_make_ellipse():

    test_image = 255 * np.random.rand(300, 600) # random 2-d array of ints

    e = ellipse.Ellipse((100,100),30, 60, test_image.shape, np.pi/6) #fix center coordinates (maybe backwards?)

    vals = np.unique(e.make_ellipse())
    assert len(vals) == 2
    assert vals[0] == 0
    assert vals[1] == 1

def test_apply_elliptical_mask():

    test_image = 255 * np.random.rand(300,600) 

    e = ellipse.Ellipse((100,100),30, 60, test_image.shape, np.pi/6) 
    e_array = e.make_ellipse() #can't think of a better name for this
    masked_image = e.apply_elliptical_mask(test_image)
     
    unmasked, masked = np.where(e_array == 1), np.where(e_array == 0)
    assert masked_image[masked].all() == 0
    assert test_image[unmasked].all() == masked_image[unmasked].all()



