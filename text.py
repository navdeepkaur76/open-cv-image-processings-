import cv2
img=cv2.imread('Candlelight.jpeg')
cv2.imshow('My Image',img)
text=cv2.putText(img, "Hello", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow('My Image',text)
cv2.waitKey(0)
cv2.destroyAllWindows()
