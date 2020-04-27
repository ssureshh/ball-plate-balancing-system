import time
import cv2
import camlib
import pidlib
import seriallib as servos
import socketlib2 as socket


def main():
    pid_x = pidlib.PID_controller("pid_x.conf")
    pid_y = pidlib.PID_controller("pid_y.conf")
    cam = camlib.camera()

    x_center = 410
    y_center = 300
    user_x = x_center
    user_y = y_center

    while 1:
        cam.calc_currentPos()
        user = socket.desired_coords()
        user_x = user['x']
        user_y = user['y']
        # print(f'userX: {user_x},userY: {user_y}')
        socket.send_coords(cam.pos_x,cam.pos_y)
        if user_x == 0 or user_y == 0:
            error_x = x_center - cam.pos_x
            error_y = y_center - cam.pos_y
        else:
            error_x = user_x - cam.pos_x
            error_y = user_y - cam.pos_y
        #print("X_error : "+str(error_x)+"| Y error : "+str(error_y))

        pid_x.compute_PID(error_x, "X")
        pid_y.compute_PID(error_y, "Y")
        # print("MAIN LOOP")
        # print("X_OUTPUT : "+str(pid_x.output)+"| Y_OUTPUT : "+str(pid_y.output))
        servos.set_angles(pid_x.output, pid_y.output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            servos.set_angles(0, 0)
            cam.reset()
            exit()
            break



if __name__ == "__main__":
    main()


"""
Notes : 

print("xxx : "+str(123))
print("xxx : "+str(123)+"| yyy : "+str(456))

"""