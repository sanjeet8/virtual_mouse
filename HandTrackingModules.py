import cv2
import time
import mediapipe as mp

class handDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

#Here  in mpHands.Hands its taking input static image mode = False that means some time it will deteact and some
#some time it will not deteact based on the confidence level. but if it is true then all time it will do deteact only 
#which will make it slow, next maxHands which is by default 2, than detectionCon which is 50% and min trackCon is 50%.
#i.e. if it will below 50% then it will start detect again.
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

        self.tipId = [4, 8, 12, 16, 20]

    def findHands(self,img, draw = True):
        #here sebding RGB image to object hands.
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Converted image into RGB images
        self.Result = self.hands.process(imgRGB)
        #print(self.Result.mult_hand_landmarks)

        #Here extreating results of each hands on handLns and mpDraw will draw the 21 landmark on original image and 
        #for for drawing connections here used mpHands.Hand_Connection.
        if self.Result.multi_hand_landmarks:
            for handLns in self.Result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLns, self.mpHands.HAND_CONNECTIONS)
        return img

    #
    def findPosition(self, img, handNo=0, draw = True):
        xList = []
        yList = []
        bBox = []
        self.lmList = []
        if self.Result.multi_hand_landmarks:
            myHand = self.Result.multi_hand_landmarks[handNo]

            # Here id will get the hand landmark id i.e. 0 - 20 and and lm will get information of the x,y,z coordinate
            # of each id number in correct order. in this i use x and y coordinate to find the location of landmark
            # of the hand by multply the height h and width w to get int value in cx, cy and put this on list lmList then return.
            for id, lm in enumerate(myHand.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                xList.append(cx)
                yList.append(cy)
                #print(id, cx, cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,0,255), cv2.FILLED)
            x_min, x_max = min(xList), max(xList)
            y_min, y_max = min(yList), max(yList)
            bBox = x_min, y_min, x_max, y_max

            if draw:
                pass
                #cv2.rectangle(img, (bBox[0] - 20, bBox[1] -20), (bBox[2]+20, bBox[3]+20), (0, 255, 0), 2)

        return self.lmList

    def fingersUp(self):
        fingers = []
        #Thumb
        if self.lmList[self.tipId[0]][1] > self.lmList[self.tipId[0]-1][1]:
                fingers.append(1)
                #print("Thumb Finger OPen")
        else:
            fingers.append(0)
        #For Other Fingers
        for id in range(1,5):
            if self.lmList[self.tipId[id]][2] < self.lmList[self.tipId[id]-2][2]:
                fingers.append(1)
                #print("Rest Finger OPen")
            else:
                fingers.append(0)
        return fingers
    

def main():
    prevTime = 0
    CurrTime = 0
    cap = cv2.VideoCapture(1)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) !=0:
            print(lmList[4])

        CurrTime = time.time()
        fps = 1/(CurrTime-prevTime)
        prevTime = CurrTime

        cv2.putText(img,str(int(fps)),(18,78), cv2.FONT_HERSHEY_PLAIN,3, (255,0,255),3)

        cv2.imshow("Hand Tracking", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
    