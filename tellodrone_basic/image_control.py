import KeyPresscontrol as kp
from djitellopy import tello
from time import sleep
import cv2

def get_keyboard_input():
    lr,fb,ud,yv = 0,0,0,0
    speed = 50
    if kp.get_key("LEFT"): lr = -speed
    elif kp.get_key("RIGHT"): lr = speed
    if kp.get_key("UP"):
        fb = speed
    elif kp.get_key("DOWN"):
        fb = -speed
    if kp.get_key("w"):
        ud = speed
    elif kp.get_key("s"):
        ud = -speed
    if kp.get_key("a"):
        yv = speed
    elif kp.get_key("d"):
        yv = -speed
    if kp.get_key("q"): mytello.land()
    if kp.get_key("e"): mytello.takeoff()

    return [lr,fb,ud,yv]
if __name__ == '__main__':

    kp.init()

    mytello = tello.Tello()
    mytello.connect()
    print(mytello.get_battery())

    mytello.streamon()

    while True:
        img = mytello.get_frame_read().frame
        img = cv2.resize(img,(360,240))
        cv2.imshow('image',img)
        values = get_keyboard_input()
        mytello.send_rc_control(values[0],values[1],values[2],values[3])
        cv2.waitKey(1)


