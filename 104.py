import cv2
import mediapipe as mp
import time
import pyautogui
mp_hands=mp.solutions.hands
hands=mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.7)
mp_draw=mp.solutions.drawing_utils
SCROLL_SPEED=50
SCROLL_DELAY=0.3
cap=cv2.VideoCapture(0)
finger_tips=[8,12,16,20]
def detect(landmarks):
    fingers=[]
    for tips in finger_tips:
        if landmarks.landmark[tips].y<landmarks.landmark[tips-2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers
last_scroll_time=time.time()
while True:
    success,img=cap.read()
    if not success:
        break
    img=cv2.flip(img,1)
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=hands.process(rgb)
    if result.multi_hand_landmarks:
        for i in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img,i,mp_hands.HAND_CONNECTIONS)
            fingers=detect(i)
            total=sum(fingers)
            cv2.putText(img,f"Fingers{total}",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),5)
            if total==5 and (time.time()-last_scroll_time)>SCROLL_DELAY:
                pyautogui.scroll(-SCROLL_SPEED)
                last_scroll_time()
    cv2.imshow("Hand Gesture Control",img)
    if cv2.waitKey(1)== ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
            

