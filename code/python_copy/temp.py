import socketlib2 as socket
from random import randrange
import time


while (1):
    x=randrange(300)
    y=randrange(300)
    socket.send_coords(x,y)
    time.sleep(1)
    print(f'DESIRED : {socket.desired_coords()}')
    print(f'PID : {socket.desired_pid()}')