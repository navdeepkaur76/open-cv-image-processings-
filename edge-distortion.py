import cv2

img = cv2.imread('candlelight.jpeg')
edges = cv2.Canny(img, 100, 200)

cv2.imshow('My Image', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
