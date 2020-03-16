import cv2
import imutils
import numpy as np

cap = cv2.VideoCapture(1)
kernel = np.ones((5,5),np.uint8)

pos_x = 0
pos_y = 0

while(1):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=800)
    frame = imutils.rotate(frame, angle=180)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_lower = (0,133,87)
    hsv_upper = (24,210,212)

    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)

    processed = cv2.bitwise_and(frame, frame, mask=mask)
    dilation = cv2.dilate(mask,kernel,iterations = 1)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
    closing = cv2.GaussianBlur(closing,(5,5),0)

    contours,hierarchy = cv2.findContours(closing, 1, 2)
    if len(contours) >= 1:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        #print("Radius : "+str(radius))
        pos_x = round(x)
        pos_y = round(y)
        print("x,y : "+str(pos_x)+","+str(pos_y))
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 35:
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (255, 0, 0), -1)
            coords = str(x)+","+str(y)
            cv2.putText(frame,  coords, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.65, (255, 255, 255), 2)
            #cv2.circle(frame, (int(frame_width/2), int(frame_height/2)), 5, (0, 0, 0), -1)
            #cv2.line(frame,(int(frame_width/2), int(frame_height/2)),center,(0,255,0),3)
            cv2.circle(frame, (392,275), 5, (0, 0, 0), -1)
            cv2.line(frame,(392,275),center,(0,255,0),3)

    #cv2.imshow('output', closing)
    cv2.imshow('raw', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()