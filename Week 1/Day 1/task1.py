import cv2
import os
img=cv2.imread('image1.jpg')
if img is None:
    print(f"Cannot open image1.jpg")
height,width=img.shape[:2]
if len(img.shape)==3:
    channels=img.shape[2]
else:
    channels=1
file_format=os.path.splitext('image1.jpg')[1].upper().replace(".","")
print("Image:",'image1.jpg')
print("Width:",width)
print("Height:",height)
print("Channels:",channels)
print("Format:",file_format)
print("-"*30)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img1=cv2.imread('gray.jpg')
cv2.imwrite("gray.jpg",gray)
height1,width1=gray.shape[:2]
file_format1=os.path.splitext('gray.jpg')[1].upper().replace(".","")
print('RGB to grayscale conversion:')
print('Height:',height1)
print('Width:',width1)
print('Channel:',1)
print('Format:',file_format1)
cv2.imshow('Gray.jpg',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
