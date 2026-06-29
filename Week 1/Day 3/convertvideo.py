import cv2
import os
cap=cv2.VideoCapture("video.mp4")
os.makedirs("frames",exist_ok=True)
count=0
while True:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imwrite(f"frames/frame_{count}.jpg",frame)
    count+=1
cap.release()