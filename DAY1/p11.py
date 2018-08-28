import cv2
img=cv2.imread("ab.jpg")
cv2.imshow("Hello World",img)
cv2.waitKey(0)
print(img.shape)
print("Height of the image: ",int(img.shape[0]),"pixels")
print("Width of the image: ",int(img.shape[1]),"pixels")
cv2.imwrite("output.jpg",img)
cv2.imwrite("output.png",img)
cv2.destroyAllWindows()