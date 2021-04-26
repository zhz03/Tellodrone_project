from djitellopy import tello
from time import sleep

if __name__ == '__main__':
    mytello = tello.Tello()
    mytello.connect()
    print(mytello.get_battery())
    mytello.takeoff()
    mytello.send_rc_control(0,50,0,0)
    sleep(2)
    mytello.send_rc_control(0,0,0,0)
    mytello.land()