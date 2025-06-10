import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open webcam ")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture")
        break
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0,20,70],dtype=np.uint8)
    upper_skin=np.array([20,255,255],dtype=np.uint8)
    mask = cv2.inRange(hsv,lower_skin,upper_skin)
    result= cv2.bitwise_and(frame,frame,mask=mask)
    contour,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if contour:
        maxc=max(contour,key=cv2.contourArea)
        x,y,w,h=cv2.boundingRect(maxc)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
        centerx=int(x+w/2)
        centery=int(y+h/2)
        cv2.circle(frame,(centerx,centery),10,(0,0,0),-1)
    cv2.imshow("original img",frame)
    cv2.imshow("filtered img",result)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()