import cv2
img=cv2.imread('Candlelight.jpeg')
cv2.imshow('My Image',img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('My Image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
