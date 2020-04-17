import socketlib as socket
from random import randrange
import time


while (1):
    x=randrange(300)
    y=randrange(300)
    socket.send_coords(x,y)
    time.sleep(0.05)