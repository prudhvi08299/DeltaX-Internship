import cv2

cap=cv2.VideoCapture("video.mp4")

width=int(cap.get(3))
height=int(cap.get(4))

out=cv2.VideoWriter("processed.mp4",cv2.VideoWriter_fourcc(*'mp4v'),30,(width,height))

while True:
    ret,frame=cap.read()

    if not ret:
        break

    cv2.rectangle(frame,(50,50),(200,150),(255,0,0),2)
    cv2.circle(frame,(350,100),40,(0,255,0),2)

    out.write(frame)

    cv2.imshow("Video",frame)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()