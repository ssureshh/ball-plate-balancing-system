import matplotlib.pyplot as plt
import random
import camlib
from itertools import count
from matplotlib.animation import FuncAnimation
# from matplotlib import style

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


if __name__ == "__main__":
    main()

# plt.style.use('fivethirtyeight')

# x_vals = []
# y_vals = []

# index = count()

# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0,100))
#     plt.cla()
#     plt.plot(x_vals, y_vals)

# ani = FuncAnimation(plt.gcf(), animate, interval=10)

# plt.tight_layout()
# plt.show()





# style.use('fivethirtyeight')
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)

# def animate(i):
#     graph_data = open('sample.txt', 'r').read()
#     lines = graph_data.split('\n')
#     xs = []
#     ys = []
#     for line in lines:
#         if len(line) > 1:
#             x, y = line.split(',')
#             xs.append(x)
#             ys.append(y)
#     ax1.clear()
#     ax1.plot(xs,ys)

# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show() x





# from matplotlib import pyplot as plt

# dev_x = [1,2,3,45,32]
# dev_y = [23,23,54,67,3]

# plt.plot(dev_x, dev_y)

# plt.title("Test")
# plt.xlabel("Time")
# plt.ylabel("value")

# plt.show()