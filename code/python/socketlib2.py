import socketio

sio = socketio.Client()
sio.connect('http://localhost:8000')

des_X = 0
des_Y = 0
# pid_gains = [
#     'x_p'= 0.0,
#     'x_i'= 0.0,
#     'x_d'= 0.0,
#     'y_p'= 0.0,
#     'y_i'= 0.0,
#     'y_d'= 0.0,
# ]

@sio.on('des_client')
def printmsg(data):
    global des_X
    global des_Y
    des_X = data['x']
    des_Y = data['y']
    # print(f'X:{des_X}, y:{des_Y}')

# @sio.on('pid_client')
# def printmsg(data):
#     global pid_gains
#     pid_gains = [
#         'x_p'= data['x_p'],
#         'x_i'= data['x_i']
#         'x_d'= data['x_d'],
#         'y_p'= data['y_p'],
#         'y_i'= data['y_i']
#         'y_d'= data['y_d'],
#     ]
#     print(f'X:{des_X}, y:{des_Y}')

def desired_coords():
    global des_X
    global des_Y
    des_xy = {
        'x': des_X,
        'y': des_Y
    }
    return des_xy
def desired_pid():
    global pid_gains
    return pid_gains

def send_coords(x, y):
    send_coords = {
        'x':x,
        'y':y
    }
    sio.emit('coord_event', send_coords)
    # print(send_coords)