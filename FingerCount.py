import cv2
import time
import os
import HandTrackingModules as htm


class Finger_Count:
    def __init__(self,root):
        self.root = root
        wCam, hCam = 640, 480

        Cap = cv2.VideoCapture(1)
        Cap.set(3, wCam)
        Cap.set(4, hCam)

        # Here importing images and stored it on list myList and saved into overlayList
        folderPath = "images"
        myList = os.listdir(folderPath)
        print(myList)
        overlayList = []
        for imgPath in myList:
            Image = cv2.imread(f'{folderPath}/{imgPath}')
            overlayList.append(Image)
        PrevTime =0
        detector = htm.handDetector(detectionCon=0.7) # here create object detector with detection confidence

        tipId = [4, 8, 12, 16, 20]

        while True:
            success, img = Cap.read()
            img = detector.findHands(img) #here detector will find images and send it to img so it will draw hand
            lmList = detector.findPosition(img, draw=False) #create list lmList of landmarks 

            # here finding fingers are open or not and save this in fingers.
            if len(lmList) != 0:
                fingers = []

                #For Thumb
                if lmList[tipId[0]][1] > lmList[tipId[0]-1][1]:
                        fingers.append(1)
                        #print("Thumb Finger OPen")
                else:
                    fingers.append(0)
                
                #For other 4 Fingers
                for id in range(1,5):
                    if lmList[tipId[id]][2] < lmList[tipId[id]-2][2]:
                        fingers.append(1)
                        #print("Index Finger OPen")
                    else:
                        fingers.append(0)
                        #print(fingers)
                totalFingers = fingers.count(1)
                print(totalFingers)

                # here slicing the images which is stored in overlayList and also independent image size in img.
                h, w, c = overlayList[totalFingers].shape
                img[0:h, 0:w] = overlayList[totalFingers]

            # here calculate the fps
            CurrTime = time.time()
            fps = 1/(CurrTime - PrevTime)
            PrevTime = CurrTime
            # Drawing FPS on images 
            cv2.putText(img, f'FPS:{int(fps)}', (400,  70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

            cv2.imshow("Finger Counter", img)
            if cv2.waitKey(1) == ord('q'):
                break

        Cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    Finger_Count()
