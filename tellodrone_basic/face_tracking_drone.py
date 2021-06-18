import cv2.cv2 as cv2
import numpy as np
from djitellopy import tello
import time

width,high = 360,240  # manually set
fbrange = [6200,6800] # manually set by human
pid = [0.4,0.4,0] # proportional p, integral i, derivative d
pError = 0

def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
    faces = faceCascade.detectMultiScale(imgGray,1.4,8)

    myFaceListC = []
    myFaceListArea =[]

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
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
    fb = 0


    if area > fbrange[0] and area < fbrange[1]:
        fb = 0
    elif area > fbrange[1]:
        fb = -20 # goback
    elif area < fbrange[0] and area!=0:
        fb = 20 # go forward

    if x == 0:
        speed = 0
        error = 0

    print("Speed:{},fb:{},".format(speed,fb))
    Drone.send_rc_control(0,fb,0,speed)

    return error

if __name__ == '__main__':

    mytello = tello.Tello()
    mytello.connect()
    print(mytello.get_battery())

    mytello.streamon()
    mytello.takeoff()
    mytello.send_rc_control(0,0,25,0)
    time.sleep(2.2)

    #mytello = "test"
    #cap = cv2.VideoCapture(0)
    while True:
        #_,img = cap.read()
        img = mytello.get_frame_read().frame

        img = cv2.resize(img,(width,high))
        img,info = findFace(img)
        pError = trackFace(mytello,info,width,pid,pError)
        print("Center:{},Area:{}".format(info[0],info[1]))
        #print(pError)
        cv2.imshow("ouput",img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            mytello.land()
            break




