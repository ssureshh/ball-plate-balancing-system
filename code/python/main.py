import camlib
import cv2
import pidlib
import seriallib as servos
import time

def main():
    pid_x = pidlib.PID_controller("pid_x.conf")
    pid_y = pidlib.PID_controller("pid_y.conf")
    cam = camlib.camera()

    x_center = 410
    y_center = 300

    while 1:
        cam.calc_currentPos()
        error_x = x_center - cam.pos_x
        error_y = y_center - cam.pos_y
        #print("X_error : "+str(error_x)+"| Y error : "+str(error_y))

        pid_x.compute_PID(error_x, "X")
        pid_y.compute_PID(error_y, "Y")
        # print("MAIN LOOP")
        # print("X_OUTPUT : "+str(pid_x.output)+"| Y_OUTPUT : "+str(pid_y.output))
        servos.set_angles(pid_x.output, pid_y.output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            servos.set_angles(0, 0)
            break



if __name__ == "__main__":
    main()


"""
Notes : 

print("xxx : "+str(123))
print("xxx : "+str(123)+"| yyy : "+str(456))

"""