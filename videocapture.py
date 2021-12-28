import numpy as np
import cv2
import time

# duration in seconds of video to be captured

capture_duration = 10
cap = cv2.VideoCapture(0)
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))

start_time = time.time()
while(int(time.time()-start_time)<capture_duration):
    ret,frame= cap.read()

    writer.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
   

cap.release()
writer.release()
cv2.destroyAllWindows()