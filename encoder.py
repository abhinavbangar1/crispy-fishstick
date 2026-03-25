import cv2 as cv
import numpy as np
from imutils import rotate

def encode_image(image):
    image = cv.imread(image)
    image = cv.cvtColor(image , cv.COLOR_RGB2GRAY)
    h,w,c = image.shape
    print(f"Image Encoded ans Saved as ${image}")


def modulation(image):
    val = np.random.randint(0 , 256 , image.shape , dtype=np.uint8) ## random int between 0 and 255 with the same shape as the image
    mul = np.random.randint(1 , 10) 
    image = (mul * image + val) % 256
    key = (val , mul)
    return image , key , "mod"

# def generate_key(op): 
#         if op == "mod_add"

def spatial_per():
    pass

def rotate() :
    pass

def shuffle():
    pass

def flipping():
    pass

def split_transform():
    pass


def confusion():
    pass

def diffuse():
    pass