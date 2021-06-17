import cv2.cv2 as cv2
import numpy as np

def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
    faces = faceCascade.detectMultiScale(imgGray,1.2,10)

    myFaceListC = []
    myFaceListArea =[]

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cx = x+w//2
        cy = y+h//2
        area = w * h
        cv2.circle(img,(cx,cy),5,(0,255,0),cv2.FILLED)
        myFaceListC.append([cx,cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img,[myFaceListC[i],myFaceListArea[i]]
    else:
        return img, [[0,0],0]


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        _,img = cap.read()
        img,info = findFace(img)
        print("Center:{},Area:{}".format(info[0],info[1]))
        cv2.imshow("ouput",img)

        cv2.waitKey(1)




