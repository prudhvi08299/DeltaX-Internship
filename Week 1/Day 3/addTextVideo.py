import cv2
cap=cv2.VideoCapture("video.mp4")
width=int(cap.get(3))
height=int(cap.get(4))
out=cv2.VideoWriter("text_video.mp4",cv2.VideoWriter_fourcc(*'mp4v'),30,(width,height))
while True:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.putText(frame,"DeltaX AI",(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    out.write(frame)
    cv2.imshow("Video",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()