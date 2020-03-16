import serial
import time

port = "/dev/cu.usbmodem14201"
baud = 115200


ser = serial.Serial(port, baud, timeout=1)

if ser.is_open:
    print(ser.name + "is open...")

def set_angles(out_x, out_y):
    cmd = str(out_x)+":"+str(out_y)+"$"
    ser.write(cmd.encode())
    print(cmd)

def close_connection():
    ser.close()
    





# def close_connection():
#     ser.close()

# while 1:
#     cmd = '10:10'
#     ser.write(cmd.encode())
#     print("HIGH")
#     time.sleep(2)
#     ser.write(b'50:50')
#     print("LOW")
#     time.sleep(2)
