import cv2
import os
from datetime import datetime
now = datetime.now() # current date and time

# Opens the Video file
cap= cv2.VideoCapture('input/play.mp4')
i=0
path = now.strftime("%Y-%m-%d_%H:%M:%S")
try:
    os.mkdir("output/"+path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite("output/"+path+"/kang"+str(i)+".jpg",frame)
    i+=1

cap.release()
cv2.destroyAllWindows()

