:orphan:

Demo: Applying an Ellipse Mask to an image
==========================================

Once you have imgmasks installed, how can you use it? Read on for an example of how to apply an elliptical mask to an image of HL Tau! (file saved in root directory)


Imports
"""""""

First we need to import all of the relevant packages:
::

        from imgmasks.ellipse import Ellipse
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg


Reading in PNG image as a grayscale array
"""""""""""""""""""""""""""""""""""""""""
This code snippet will read in any PNG as an array that is passable to apply_elliptical_mask, but you can use any image in the form of a 2D array. 
::

        png = mpimg.imread("hltau225.png")
        if len(png.shape)==3:  # if image is in RGB
                img = np.dot( png[...,:3], [0.2989, 0.5870, 0.1140]) 
        elif len(img.shape)==2: # if image is already in grayscale
                img = png
        plt.imshow(img, cmap = "gray")
        plt.show()

Generating Elliptical Mask
""""""""""""""""""""""""""
Initialize the Ellipse object with input parameters:
::

        e = Ellipse((112,112), 90, 60, (225, 225), theta=45)

Create an ellipse mask array -- the output array represents a grid of pixels where pixels inside the ellipse have value 1 and pixels outside the ellipse have value 0.         
::

        mask_array = e.make_ellipse()


Applying the Mask
"""""""""""""""""
        
Apply the mask to the image:
::

        masked_image = e.apply_elliptical_mask(img)
        plt.imshow(masked_image, cmap = "gray")
        plt.show()

Save your image:
::
        
        plt.savefig("hltau225_masked.png")
