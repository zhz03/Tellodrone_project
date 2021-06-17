import cv2.cv2 as cv2
import numpy as np


fbrange = [6200,6800] # manually set by human
pid = [0.4,0.4,0] # proportional p, integral i, derivative d
pError = 0

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

def trackFace(Drone,info,width,pid,pError):

    area = info[1]
    x,y = info[0]
    COI = width//2 # center of the image
    error = x - COI
    speed = pid[0] * error + pid[1] * (error-pError)
    speed = int(np.clip(speed,-100,100))


    if area > fbrange[0] and area < fbrange[1]:
        fb = 0
    elif area > fbrange[1]:
        fb = -20 # goback
    elif area < fbrange[0] and area!=0:
        fb = 20 # go forward

    #Drone.send_rc_control(0,fb,0,speed)

    return error

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        _,img = cap.read()
        img,info = findFace(img)
        pError = trackFace(Drone,info,width,pid,pError)
        print("Center:{},Area:{}".format(info[0],info[1]))
        cv2.imshow("ouput",img)

        cv2.waitKey(1)




