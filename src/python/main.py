import camlib
import cv2
import pidlib
import serial_com as servos
import time

def main():
    pid_x = pidlib.PID_controller()
    pid_y = pidlib.PID_controller()
    cam = camlib.camera()

    x_center = 414
    y_center = 310

    while 1:
        cam.calc_currentPos()
        error_x = x_center - cam.pos_x
        error_y = y_center - cam.pos_y
        #print("X_error : "+str(error_x)+"| Y error : "+str(error_y))
        pid_x.compute_PID(error_x, "X_AXIS")
        pid_y.compute_PID(error_y, "==Y_AXIS")
        # print("X_output : "+str(pid_x.output)+"| Y output : "+str(pid_y.output))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == "__main__":
    main()


"""
Notes : 

print("xxx : "+str(123))
print("xxx : "+str(123)+"| yyy : "+str(456))

"""