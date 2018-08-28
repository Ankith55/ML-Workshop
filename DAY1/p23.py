import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.putText(img,'Ankith',(60,350),cv2.FONT_HERSHEY_COMPLEX,3,(170,170,170),3)
cv2.imshow('Text',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
