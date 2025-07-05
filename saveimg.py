import cv2
img=cv2.imread('Candlelight.jpeg')
cv2.imshow('My Image',img)
save=cv2.imwrite('output.jpg', img)
cv2.imshow('My Image',save)
cv2.waitKey(0)
cv2.destroyAllWindows()
