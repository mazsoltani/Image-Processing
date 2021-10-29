import cv2

img=cv2.imread('Ronaldoo.jpg',0)
height,width=img.shape
for i in range(height):
    for j in range(width):
        img[i,j]=255-img[i,j]

cv2.imshow('CR7',img)
cv2.imwrite('Ronaldo.jpg',img)

cv2.waitKey()
