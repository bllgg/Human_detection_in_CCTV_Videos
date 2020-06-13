import cv2
import os
#from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
from datetime import datetime
now = datetime.now() # current date and time
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
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
    #print(type(frame))
    image = imutils.resize(frame, width=min(400, frame.shape[1]))
    orig = image.copy()   
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
		padding=(8, 8), scale=1.05)
    if (len(rects) > 0):
        for (x, y, w, h) in rects:
            cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

        cv2.imwrite("output/"+path+"/frame"+str(i)+".jpg",image)

    
    #cv2.imwrite("output/"+path+"/kang"+str(i)+".jpg",frame)
    i+=1

cap.release()
cv2.destroyAllWindows()

