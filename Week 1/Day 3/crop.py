import cv2

img=cv2.imread("image1.jpg")

crop=img[50:350,100:500]

cv2.imshow("Crop",crop)
cv2.imwrite("crop.jpg",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()