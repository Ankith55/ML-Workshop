import cv2
import numpy as np
img=cv2.imread('ab.jpg')
height,width=img.shape[:2]
ar,ac=int(height*.1),int(width*.1)
sr,sc=int(height*.25),int(width*.25)
er,ec=int(height*.5),int(width*.5)
mr,mc=int(height*.75),int(width*.75)

br,bc=int(height*.25),int(width*.25)
rr,rc=int(height*.5),int(width*.5)
fr,fc=int(height*.75),int(width*.75)
nr,nc=int(height*1),int(width*1)
im=img[ar:br,ac:bc]
im1=img[sr:rr,sc:rc]
im2=img[er:fr,ec:fc]
im3=img[mr:nr,mc:nc]
cv2.imshow('Image',im)
cv2.imshow('Image1',im1)
cv2.imshow('Image2',im2)
cv2.imshow('Image3',im3)
cv2.waitKey(0)
cv2.destroyAllWindows()
