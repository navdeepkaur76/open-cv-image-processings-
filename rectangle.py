import cv2
img=cv2.imread('Candlelight.jpeg')
cv2.imshow('My Image',img)

rectangle=cv2.rectangle(img,(50,50),(200,200),(0,255,0),2)
cv2.imshow('My Image',rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()
