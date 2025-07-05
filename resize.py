import cv2
img=cv2.imread('Candlelight.jpeg')
cv2.imshow('My Image',img)
resized=cv2.resize(img,(300,300))
cv2.imshow('My Image',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
