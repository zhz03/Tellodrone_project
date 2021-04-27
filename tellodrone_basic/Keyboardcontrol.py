import KeyPresscontrol as kp
from djitellopy import tello
from time import sleep

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

    #mytello.takeoff()

    while True:
        values = get_keyboard_input()
        mytello.send_rc_control(values[0],values[1],values[2],values[3])
        sleep(0.05)

        #print(kp.get_key("s"))