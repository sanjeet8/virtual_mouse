import cv2
import numpy as np
import time
import math
import pyautogui
import HandTrackingModules as htm

class Virtual_Mouse:
    def __init__(self,root):
        self.root = root
        # Frame Setting
        #########################################
        wCam, hCam = 1200, 700
        wframeRed = 400
        hframeRed = 200
        smooth = 4
        #########################################

        PrevTime = 0
        PrevLocX, PrevLocY = 0, 0
        CurrLocX, CurrLocY = 0, 0

        # Opening the device camera for taking live input
        WebCam = cv2.VideoCapture(1)
        WebCam.set(3, wCam)
        WebCam.set(4, hCam)
        #Creating object
        detector = htm.handDetector(maxHands=2)
        detector = htm.handDetector(detectionCon=0.7)
        tipId = [4, 8, 12, 16, 20]
        widScr, higScr = pyautogui.size() #1362, 768
        #print(widScr, higScr)

        while True:
            #1. Find hand landmarks
            #Reading live Image and returning
            success, img = WebCam.read()
            #img = cv2.flip(img, 1) #Flip The Image So that avoid Resersing
            img = detector.findHands(img)
            #Finding Position of hand and stored into img
            lmList = detector.findPosition(img) 

            #Set Frame for mouse cursor movement in that fram 
            TouchPad = cv2.rectangle(img, (300, 80), (wCam - wframeRed, hCam - hframeRed), (150,160,255), 3)
            cv2.putText(img, "Touch Pad", (450, hCam - hframeRed + 25), cv2.FONT_HERSHEY_PLAIN, 2, (0,200,250), 3)

            #2. Get the tip of the middle and index fingre for mouse movement and left click
            if len(lmList) != 0:
                x1, y1 = lmList[8][1:]
                x2, y2 = lmList[12][1:]

                #3. Check which fingers are up
                if len(lmList) != 0:
                    fingers = detector.fingersUp()
                totalFingers = fingers.count(1)
                #print(totalFingers)

                #4. When Only index fingure is Up then Mouse Cursor Moving
                if fingers[1] == 1 and fingers[2] == 0:

                    #5. Converting Coordinates
                    x3 = np.interp(x1, (450, wCam -100 - wframeRed), (0, widScr))
                    y3 = np.interp(y1, (150, hCam -150 - hframeRed), (0, higScr))

                    #6. Smoothen Values so that mouse cursor move step by step  not directly.
                    CurrLocX = PrevLocX + (x3 - PrevLocX) / smooth
                    CurrLocY = PrevLocY + (y3 - PrevLocY) / smooth

                    #7. Mouse movment 
                    # Here in moveTo(widScr - CurrLocX, CurrLocY) widScr - CurrLocX is used to flip the value
                    # so when our hand moves left then cursor will also move towards left and vise versa.
                    pyautogui.moveTo(widScr - CurrLocX, CurrLocY)
                    cv2.circle(img, (x1, y1), 15, (255,0,0), cv2.FILLED)
                PrevLocX, PrevLocY = CurrLocX, CurrLocY

                if fingers[0] == 1:
                    x5 = np.interp(x1, (450, wCam -100 - wframeRed), (0, widScr))
                    y5 = np.interp(y1, (150, hCam -150 - hframeRed), (0, higScr))
                    CurrLocX = PrevLocX + (x5 - PrevLocX) / smooth
                    CurrLocY = PrevLocY + (y5 - PrevLocY) / smooth
                    pyautogui.scroll(10,widScr - CurrLocX, CurrLocY)
                PrevLocX, PrevLocY = CurrLocX, CurrLocY

                if fingers[0] == 1 and fingers[1] == 1:
                    #9. Find Distance between Fingers
                    x0, y0 = lmList[4][1], lmList[4][2]
                    x1, y1 = lmList[8][1], lmList[8][2]
                    
                    cx, cy = (x0+x1)//2, (y0+y1)//2
                    cv2.circle(img, (x0,y0), 15, (255,0,255), cv2.FILLED)
                    cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)
                    cv2.line(img, (x0,y0), (x1,y1), (255, 0, 255), 3)
                    cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)
                    length = math.hypot(x1-x0, y1-y0)
                    #print(length)
                        
                    #10. Right Click Mouse If Distance Short
                    if length < 30:
                        cv2.circle(img, (cx,cy), 15, (0,255,200), cv2.FILLED)
                        pyautogui.click(button='right', duration=0.2)

                #8. Both Index And Middle Fingres Are Up : Left Clicking Mode
                if fingers[1] == 1 and fingers[2] == 1:
                    #9. Find Distance between Fingers
                    x1, y1 = lmList[8][1], lmList[8][2]
                    x2, y2 = lmList[12][1], lmList[12][2]
                    cx, cy = (x1+x2)//2, (y1+y2)//2
                    cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)
                    cv2.circle(img, (x2,y2), 15, (255,0,255), cv2.FILLED)
                    cv2.line(img, (x1,y1), (x2,y2), (255, 0, 255), 3)
                    cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)
                    length = math.hypot(x2-x1, y2-y1)
                    #print(length)
                    
                    #10. Left Click Mouse If Distance Short
                    if length < 25:
                        cv2.circle(img, (cx,cy), 15, (0,255,0), cv2.FILLED)
                        pyautogui.click(duration=0.2)

                if fingers[0] == 1:
                    cv2.circle(img, (cx,cy), 15, (0,255,200), cv2.FILLED)
                    pyautogui.doubleClick()
                    #PrevLocX, PrevLocY = CurrLocX, CurrLocY
            
            #11. Frame Rate
            CurrTime = time.time()
            fps = 1/(CurrTime - PrevTime)
            PrevTime = CurrTime
            cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3)

            #12. Display
            cv2.imshow("WebCam", img)
            if cv2.waitKey(1) == ord('q'):
                break

        WebCam.release()
        cv2.destroyAllWindows()
  

if __name__ == "__main__":
    Virtual_Mouse()