import cv2
import mediapipe as mp
import screen_brightness_control as sbc
import numpy
import math
mp_hands=mp.solutions.hands
hands=mp_hands.Hands()
mp_draw=mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)
while True:
    success,image=cap.read()
    rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    result=hands.process(rgb)
    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            lm_list=[]
            for id, lm in enumerate(handlms.landmark):
                h,w,c=image.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lm_list.append((cx,cy))
            if lm_list:
                x1,y1=lm_list[4]
                x2,y2=lm_list[8]
                length=math.hypot(x2-x1,y2-y1) 
                brightness=int(max(0,min(100,(length-30)*2)))
                sbc.set_brightness(brightness)
                cv2.circle(image,(x1,y1),10,(255,0,0),cv2.FILLED)
                cv2.circle(image,(x2,y2),10,(255,0,0),cv2.FILLED)
                cv2.line(image,(x1,y1),(x2,y2),(0,255,0),3)
                cv2.putText(image,f"brightness : {brightness}",(50,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,255,255),2)
            mp_draw.draw_landmarks(image,handlms,mp_hands.HAND_CONNECTIONS)
    
    cv2.imshow("Gesture Control",image)
    if cv2.waitKey(1) & 0xFF == ord("q")  :
        break    
                        
