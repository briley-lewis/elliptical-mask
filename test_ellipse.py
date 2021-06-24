#end to end test of ellipse mask
import ellipse
import numpy as np
import matplotlib.pyplot as plt

test_image = 255 * np.random.rand(300,600)

e = ellipse.Ellipse((100,100),30, 60, test_image.shape, np.pi/6) #fix center coordinates (maybe backwards?)

vals = np.unique(e.make_ellipse())
assert len(vals) == 2
assert vals[0] == 0
assert vals[1] == 1

masked_image = e.apply_elliptical_mask(test_image)

##uncomment these if you want to see the test plot!
##plt.imshow(masked_image,origin='lower')

#plt.colorbar()
#plt.savefig("mask_test.png")
#plt.show()