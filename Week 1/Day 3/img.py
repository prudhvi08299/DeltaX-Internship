import cv2
img=cv2.imread("image.jpg")

cv2.putText(img,"DeltaX AI Internship",(40,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

cv2.imshow("Text",img)
cv2.imwrite("text_image.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()