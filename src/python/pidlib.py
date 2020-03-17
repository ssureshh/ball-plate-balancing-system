import re
import time

class PID_controller(object):
    def __init__(self,filename,current_time=None):
        file = open(filename,"r")
        lines = file.readlines()
        kp=float(re.split(':',lines[0])[1])
        ki=float(re.split(':',lines[1])[1])
        kd=float(re.split(':',lines[2])[1])
        out_min=float(re.split(':',lines[3])[1])
        out_max=float(re.split(':',lines[4])[1])
        file.close()
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.out_min = out_min
        self.out_max = out_max
        print("PID "+"["+str(filename)+"]"+ " = ("+str(self.kp)+")("+str(self.ki)+")("+str(self.kd)+")")
        self.sample_time = 0.00
        self.current_time = current_time if current_time is not None else time.time()
        self.previous_time = self.current_time
        self.last_error = 0.00
        self.cumulative_error = 0.00
        self.output = 0.00
        self.output = 0.00

    def compute_PID(self,error,name,current_time=None):
        #print("Error : "+str(error))
        self.current_time = current_time if current_time is not None else time.time()
        elasped_time = self.current_time - self.previous_time
        #print("AXIS : "+str(name)+"| current_time : "+str(self.current_time)+"| elapsed_time : "+str(elasped_time)+"| previous_time : "+str(self.previous_time))

        self.cumulative_error += error*elasped_time
        self.rate_error = (error - self.last_error)/elasped_time
        #print(str(name)+" => "+"cumErr : "+str(self.cumulative_error)+" | rateErr : "+str(self.rate_error))

        if self.cumulative_error > 20:
            self.cumulative_error = 20
        if self.cumulative_error < -20:
            self.cumulative_error = -20
        #print(str(name)+" => "+"cumErr : "+str(self.cumulative_error)+" | rateErr : "+str(self.rate_error))

        self.output = self.kp*error + self.ki*self.cumulative_error + self.kd*self.rate_error
        # print(str(name)+" : "+str(self.output))
        
        self.last_error = error
        self.previous_time = self.current_time

        # print("OUT : "+str(self.out_max))
        #print("["+str(name)+"]"+"OUT : "+str(self.output))

        if self.output > self.out_max:
            self.output = self.out_max
        if self.output < self.out_min:
            self.output = self.out_min
        print("["+str(name)+"]"+"OUT : "+str(self.output))

    