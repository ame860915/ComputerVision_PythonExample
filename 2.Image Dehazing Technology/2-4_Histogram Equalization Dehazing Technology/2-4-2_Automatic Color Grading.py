import numpy as np 
import cv2

img = cv2.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\Lenna.bmp", 0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cll = clahe.apply(img)
cv2.imshow('img', img)
cv2.imshow('cll', cll)
cv2.waitKey(0)
cv2.destroyAllWindows()