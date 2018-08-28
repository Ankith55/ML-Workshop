import cv2
img=cv2.imread('ab.jpg')
B,G,R=img[0,0]
print(B,G,R)
print(img.shape)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)
print(gray[0,0])
ret, th =cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
print(th.shape)
print(th[0,0])
