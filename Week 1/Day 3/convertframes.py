import cv2
import os
folder="frames"
images=sorted(os.listdir(folder))
frame=cv2.imread(os.path.join(folder,images[0]))
height,width,_=frame.shape
video=cv2.VideoWriter("output.mp4",cv2.VideoWriter_fourcc(*'mp4v'),30,(width,height))
for img in images:
    frame=cv2.imread(os.path.join(folder,img))
    video.write(frame)
video.release()