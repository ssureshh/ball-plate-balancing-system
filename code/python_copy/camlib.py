import cv2
import imutils
import numpy as np
import re

class camera:

    # Class variables for the camera class
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0

        file = open("variables.conf","r")
        lines = file.readlines()
        hl=re.split(':',lines[0])[1]
        hh=re.split(':',lines[1])[1]
        sl=re.split(':',lines[2])[1]
        sh=re.split(':',lines[3])[1]
        vl=re.split(':',lines[4])[1]
        vh=re.split(':',lines[5])[1]
        file.close()

        self.hsvLow = (int(hl),int(sl),int(vl))
        self.hsvUp = (int(hh),int(sh),int(vh))
        #self.hsvLow = (24,210,212)
        #self.hsvUp = (24,210,212)
        self.capture = cv2.VideoCapture(1)
        self.kernel = np.ones((5,5),np.uint8)
    
    # func. to open cam, process and find the x,y of ball
    def calc_currentPos(self):
        (ret, frame) = self.capture.read()
        if not ret:
            exit(-1)
        
        # image processing codes
        frame = imutils.resize(frame, width=800)
        frame = imutils.rotate(frame, angle=180)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.hsvLow, self.hsvUp)
        processed = cv2.bitwise_and(frame, frame, mask=mask)
        dilation = cv2.dilate(mask,self.kernel,iterations = 1)
        closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, self.kernel)
        closing = cv2.GaussianBlur(closing,(5,5),0)

        # finding blob and finding x,y
        contours,hierarchy = cv2.findContours(closing, 1, 2)
        if len(contours) >= 1:
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            self.pos_x = round(x)
            self.pos_y = round(y)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 35:
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                cv2.circle(frame, center, 5, (255, 0, 0), -1)
                coords = str(self.pos_x)+","+str(self.pos_y)
                cv2.putText(frame,  coords, (int(self.pos_x), int(self.pos_y)), cv2.FONT_HERSHEY_SIMPLEX,0.65, (0, 0, 0), 2)
                # cv2.circle(frame, (self.setX,self.setY), 5, (0, 0, 0), -1)
                # cv2.line(frame,(self.setX,self.setY),center,(0,255,0),3)

        # show the video
        cv2.imshow("Main", frame)

    # func. to close camera feed
    def reset(self):
        self.capture.release()
        cv2.destroyAllWindows()