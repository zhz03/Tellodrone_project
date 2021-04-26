from djitellopy import tello
import cv2

if __name__ == '__main__':
    mytello = tello.Tello()
    mytello.connect()
    print(mytello.get_battery())

    mytello.streamon()

    while True:
        img = mytello.get_frame_read().frame
        img = cv2.resize(img,(360,240))
        cv2.imshow('image',img)
        cv2.waitKey(1)