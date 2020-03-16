import re

class pid_controller(object):
    def __init__(self):
        file = open("variables.conf","r")
        lines = file.readlines()
        kp=float(re.split(':',lines[7])[1])
        ki=float(re.split(':',lines[8])[1])
        kd=float(re.split(':',lines[9])[1])
        out_min=re.split(':',lines[10])[1]
        out_max=re.split(':',lines[11])[1]
        file.close()
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.out_min = out_min
        self.out_max = out_max

    def compute_pid(self,error):
        p_correction = self.kp * error

        i_correction
        
        d_correction
        
        

    