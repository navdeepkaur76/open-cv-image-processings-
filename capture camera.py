import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
if ret:
    cv2.imshow("Captured Image", frame)
    cv2.imwrite("captured.jpg", frame)

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
