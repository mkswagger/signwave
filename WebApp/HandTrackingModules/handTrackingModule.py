import cv2
import mediapipe as mp
import time
import math

class HandDetector():
    def __init__(self, mode=False, maxHands=2,modelComplexity=1, detectionCon=0.5, trackingCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon
        
        self.mpHand = mp.solutions.hands
        self.hands = self.mpHand.Hands(self.mode, self.maxHands,self.modelComplexity,
                                       self.detectionCon, self.trackingCon)
        self.mpDraw = mp.solutions.drawing_utils
        
        self.tipIds = [4,8,12,16,20]

    def findHands(self, img, draw=True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLMS in self.results.multi_hand_landmarks:
                if draw:              
                    self.mpDraw.draw_landmarks(img, handLMS, 
                                               self.mpHand.HAND_CONNECTIONS)
    
        return img
    
    def findPosition(self, img, handNo=0, drawLm = True, drawBoundingBox = True):
        
        xList = []
        yList = []
        
        boundingBox = []
        
        self.lmList = []
        
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            
            for id, lm in enumerate(myHand.landmark):
                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                
                xList.append(cx)
                yList.append(cy)
                
                self.lmList.append([id,cx,cy])
                
                # print(id, cx, cy)
                if drawLm:
                    cv2.circle(img, (cx,cy), 10, (255,0,255), cv2.FILLED)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            boundingBox = xmin, ymin, xmax, ymax

            if drawBoundingBox:
                cv2.rectangle(img, (boundingBox[0]-20, boundingBox[1]-20), (boundingBox[2]+20, boundingBox[3]+20), (0,255,0), 2)

        return self.lmList, boundingBox


    def fingersUp(self, mirrored = False):
        fingers = []
        
        # THUMB
        if mirrored:
            if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        else:
            if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        # FOUR FINGERS
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id]-3][2]:
                fingers.append(1)
            else:
                fingers.append(0)
            
        
        totalFingers = fingers.count(1)
        
        
        return fingers


    def findDisctance(self, point1, point2, img, draw=True):
        
        x1, y1 = self.lmList[point1][1], self.lmList[point1][2]
        x2, y2 = self.lmList[point2][1], self.lmList[point2][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
            
        
        if draw:
            
            cv2.circle(img, (x1,y1), 7, (255,0,255), cv2.FILLED)
            cv2.circle(img, (x2,y2), 7, (255,0,255), cv2.FILLED)
            cv2.line(img,(x1,y1),(x2,y2),(255,0,255),2)
            cv2.circle(img,(cx,cy),5,(255,0,255), cv2.FILLED)
        
        length = math.hypot(x2-x1, y2-y1)

        return length, img, [x1, y1, x2, y2, cx, cy]


def main():
    
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0

    detector = HandDetector()

    while True:
        success, img = cap.read()
        
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        
        if len(lmList) !=0:
            
            detector.fingersUp()
            print(lmList[4])
        
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), thickness=3)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)






if __name__ == "__main__":
    main()