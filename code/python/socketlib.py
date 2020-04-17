from socketIO_client import SocketIO, LoggingNamespace
import json

socketIO = SocketIO('localhost', 8000, LoggingNamespace)

def send_coords(x, y):
    send_coords = {
        'x':x,
        'y':y
    }
    socketIO.emit('coord_event', send_coords)
    print(send_coords)

def sock_print(text):
    socketIO.emit('text', text)
    print(text)