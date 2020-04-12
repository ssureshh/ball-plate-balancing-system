import camlib
import cv2
import pid
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
# import serial_com as servos

def main():
    # while 1:
    #     servos.set_angles(10,10)
    #     time.sleep(0.25)
    #     servos.set_angles(60,60)
    #     time.sleep(0.25)
    # servos.close_connection()
    
    # pid_x = pid.pid_controller()
    fig = plt.figure()
    

    cam = camlib.camera()
    while 1:
        cam.calc_currentPos()
        print(str(cam.pos_x)+","+str(cam.pos_y))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.reset()

if __name__ == "__main__":
    main()
