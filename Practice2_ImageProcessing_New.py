import numpy
import cv2

img_Jordan = cv2.imread('M_Jordan.jpg')
convert_image = cv2.cvtColor(img_Jordan, cv2.COLOR_BGR2GRAY)
cv2.imwrite('Jordan_Res.png',convert_image )

cv2.waitKey()

# باکمک از سایت زیر
# https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method/