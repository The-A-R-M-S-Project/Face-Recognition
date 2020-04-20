import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while(True):
    # capture frame by frame
    ret, frame = cap.read()

    # convert captured image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # find all faces in captured frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # face location in the window
    for (x,y,z,h) in faces:
        # from greyscale image
        g_region_of_interest = gray[y:y+h, x:x+z] # [ycord_start:ycord_end, xcord_start:xcord_end]
        # from coloured image
        c_region_of_interest = frame[y:y+h, x:x+z]
        img_item = "my-image.png"
        cv2.imwrite(img_item, g_region_of_interest)

        # draw detection rectangle
        color = (0,255,0)
        stroke = 3
        endcordx = x+z
        endcordy = y+h
        cv2.rectangle(frame, (x,y), (endcordx, endcordy), color, stroke)


    # display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
 
# when everything's done, release the capture
cap.release()
cv2.destroyAllWindows()
