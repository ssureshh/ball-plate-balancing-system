import camlib
import cv2
import pid
# import serial_com as servos
import time

def main():
    # while 1:
    #     servos.set_angles(10,10)
    #     time.sleep(0.25)
    #     servos.set_angles(60,60)
    #     time.sleep(0.25)

    cam = camlib.camera()
    # pid_x = pid.pid_controller()

    while 1:
        cam.calc_currentPos()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.reset()
    # servos.close_connection()

    





if __name__ == "__main__":
    main()
