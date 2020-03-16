def initVals(self):
    self.vals = arr.array('i')
    with open("variables.conf") as var:
        for i in var:
            a=i.split(':')
            self.vals.append(int(a[1]))
        var.close() 
    for j in range(0,9):
        print("Line-"+str(j)+" : "+str(self.vals[j]))


import re

file = open("hsv.config","r")
lines = file.readlines()
a=re.split(':',lines[0])[1]
b=re.split(':',lines[1])[1]
c=re.split(':',lines[2])[1]
d=re.split(':',lines[3])[1]
e=re.split(':',lines[4])[1]
f=re.split(':',lines[5])[1]

print(str(a))
print(str(b))
print(str(c))
print(str(d))
print(str(e))
print(str(f))