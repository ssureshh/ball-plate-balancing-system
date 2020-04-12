from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import camlib
import cv2
import pid

def main():
    fig = plt.figure()
    line, = plt.plot([], [], lw=2)
    cam = camlib.camera()
    while 1:
        cam.calc_currentPos()
        print(str(cam.pos_x)+","+str(cam.pos_y))

        ani = FuncAnimation(fig, animate, fargs=(cam.pos_x,cam.pos_y),frmaes=100, interval=100)
        plt.show()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.reset()

def animate(frame, pos_x, pos_y):
    line.set_data(pos_x, pos_y)
    return line,

if __name__ == "__main__":
    main()