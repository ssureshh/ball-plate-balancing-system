import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import camlib
import cv2

fig = plt.figure()
ax = plt.axes()
line, = ax.plot([], [], lw=2)

cam = camlib.camera()

def init():
    line.set_data([], [])
    return line,

def animate(i):
    cam.calc_currentPos()
    print(str(cam.pos_x)+","+str(cam.pos_y))
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(cam.pos_x, 400)
    return line,

# cam.calc_currentPos()
# print(str(cam.pos_x)+","+str(cam.pos_y))
anim = animation.FuncAnimation(fig, animate, init_func=init,
                            frames=200, interval=20, blit=True)
plt.show()
