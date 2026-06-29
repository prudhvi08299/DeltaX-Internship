import cv2

img=cv2.imread("image1.jpg")

roi=img[15:120,70:190]

cv2.imshow("ROI",roi)
cv2.imwrite("roi.jpg",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()