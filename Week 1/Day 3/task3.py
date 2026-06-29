import cv2
import numpy as np
img=np.ones((500,500,3),dtype=np.uint8)*255
cv2.rectangle(img,(50,50),(200,150),(255,0,0),2)
cv2.circle(img,(350,100),50,(0,255,0),2)
cv2.line(img,(50,250),(450,250),(0,0,255),2)
pts=np.array([[300,300],[400,400],[200,400]],np.int32)
cv2.polylines(img,[pts],True,(255,0,255),2)
cv2.imshow("Shapes",img)
cv2.imwrite("shapes.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()