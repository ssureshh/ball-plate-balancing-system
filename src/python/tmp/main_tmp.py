import camlib
import cv2
import pid
# import serial_com as servos
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def main():
    # while 1:
    #     servos.set_angles(10,10)
    #     time.sleep(0.25)
    #     servos.set_angles(60,60)
    #     time.sleep(0.25)
    # servos.close_connection()
    
    # pid_x = pid.pid_controller()

    cam = camlib.camera()
    while 1:
        cam.calc_currentPos()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.reset()

def animate(i):
    xs = []
    ys = []
    xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs,ys)


if __name__ == "__main__":
    main()
