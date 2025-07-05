import cv2
img=cv2.imread('Candlelight.jpeg')
cv2.imshow('My Image',img)

circle=cv2.circle(img,(150,150),50,(255,0,0),-1)
cv2.imshow('My Image',circle)
cv2.waitKey(0)
cv2.destroyAllWindows()
