import stitching
from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

def plot_image(img, figsize_in_inches=(5,5)):
    fig, ax = plt.subplots(figsize=figsize_in_inches)
    ax.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.show()

settings = {# The whole plan should be considered
            "crop": False,
            # The matches confidences aren't that good
            "confidence_threshold": 0.5} 

stitcher = stitching.Stitcher(**settings)
panorama = stitcher.stitch(["img1.jpeg", "img2.jpeg", "img3.jpeg","img4.jpeg"]) # name your images

# panorama = stitcher.stitch(["img?.jpg"])
   
# settings = {"detector": "sift", "confidence_threshold": 0.2}
# stitcher = Stitcher(**settings)
# panorama = stitcher.stitch(my_imgs)
plot_image(panorama, (20,20))
