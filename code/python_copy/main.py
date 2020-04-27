import time
import cv2
import camlib
import pidlib
import seriallib as servos


def main():
    pid_x = pidlib.PID_controller("pid_x.conf")
    pid_y = pidlib.PID_controller("pid_y.conf")
    cam = camlib.camera()

    x_center = 410
    y_center = 300

    fx = open("data_x.csv", "a+")
    fy = open("data_y.csv", "a+")

    x_index=0
    y_index=0
    while 1:
        cam.calc_currentPos()

        named_tuple = time.localtime()
        time_string = time.strftime("%H:%M:%S", named_tuple)

        fx.write(f'{time_string},{x_index},{cam.pos_x},{410}\n')
        fy.write(f'{time_string},{y_index},{cam.pos_y},{300}\n')

        error_x = x_center - cam.pos_x
        error_y = y_center - cam.pos_y
        pid_x.compute_PID(error_x, "X")
        pid_y.compute_PID(error_y, "Y")
        servos.set_angles(pid_x.output, pid_y.output)

        x_index+=1
        y_index+=1

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