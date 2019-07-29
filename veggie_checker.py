import cv2 as cv
import numpy as np
from PIL import Image

img = Image.open('images/tush.jpg')
img = np.array(img)
ir, ir_n_g, ir_n_r = cv.split(img)

bottom = ir_n_r
bottom[bottom == 0] = 0.01

ndvi = ((ir + ir) - ir_n_r)/(bottom)

while True:
    cv.imshow('', ndvi)
    
    if cv.waitKey(0) == ord('q'):
        break
        
cv.destroyAllWindows()
