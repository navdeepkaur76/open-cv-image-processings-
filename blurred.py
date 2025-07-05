import cv2

img = cv2.imread('candlelight.jpeg')
blurred = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow('My Image', blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
