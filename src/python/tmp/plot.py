import matplotlib.pyplot as plt
import random
from itertools import count
import matplotlib.animation as animation
# from matplotlib import style


plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))
    plt.plot(x_vals, y_vals)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.plot(x_vals, y_vals)



plt.tight_layout()
plt.show()








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