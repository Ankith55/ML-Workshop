import cv2
img=cv2.imread("ab.jpg",0)
ret,th=cv2.threshold(img,125,255,cv2.THRESH_BINARY)
ret,th1=cv2.threshold(img,125,255,cv2.THRESH_BINARY_INV)
cv2.imshow("HELLO",img)
cv2.imshow("HELLO",th)
cv2.imshow("HELLO",th1)
cv2.waitKey(0)
cv2.destroyAllWindows()
