import sys
import os
import random
#base class of all jobs
class Job:
    def __init__(self, Para):
	if self.__CheckParameters__(Para) is False:
	# interesting point here, python will actually call the __CheckParameters__ of subclass,
	# So you don't have to call __CheckParameters__ in subclass initialization again!
	    print "Something is wrong with the inlist! Abandon!"
	    sys.exit()
	self.Duplicate=Para.pop("__Duplicate")
	self.Execute=os.path.abspath(Para.pop("__Execute"))
	self.IsCluster=Para.pop("__IsCluster")
	self.KeepCPUBusy=True
	self.PID=0
	self.Para=Para

    def __CheckParameters__(self,Para):
	if Para["__Execute"]=="":
	    print "Please specify the executive file name!"
	    return False
	return True
	if type(Para["IsLoad"]) is not bool:
	    print "IsLoad should be a bool!"
	    return False
	return True

    def KeyToString(self,key):
	if type(self.Para[key])==bool:
	    if self.Para[key]:
		return ".true.    #{}\n".format(key)
	    else:
		return ".false.    #{}\n".format(key)
	elif type(self.Para[key])==str:
	    return self.Para[key]+"\n"
	elif type(self.Para[key])==list:
	    return "{}    #{}\n".format(",".join([str(elem) for elem in self.Para[key]]),key)
	else:
	    return "{}    #{}\n".format(self.Para[key],key)

    def ToString(self,PID=0):
	self.Para["PID"]=PID
	InputStr=self.KeyToString("PID")
	InputStr+=self.KeyToString("Lx")
	InputStr+=self.KeyToString("Ly")
	InputStr+=self.KeyToString("Jcp")
	InputStr+=self.KeyToString("Beta")
	InputStr+=self.KeyToString("Order")
	InputStr+=self.KeyToString("IsLoad")
	return InputStr

class JobMonteCarlo(Job):
    def __init__(self, Para):
	Job.__init__(self, Para)
	self.KeepCPUBusy=True
	self.Para["Type: MC"]=2

    def __CheckParameters__(self,Para):
	if Job.__CheckParameters__(self,Para) is False:
	    return False
	if type(Para["Reweight"]) is not list:
	    print "The Reweight should be a list!"
	    return False
	if Para["Order"] is not len(Para["Reweight"]):
	    print "The Reweight numbers should be equal to Order!"
	    return False
	if type(Para["IsForever"]) is not bool:
	    print "IsForever should be a bool!"
	    return False

    def ToString(self,PID=0):
	InputStr=Job.ToString(self,PID)
	InputStr+=self.KeyToString("Type: MC")
	InputStr+=self.KeyToString("IsForever")
	InputStr+=self.KeyToString("Toss")
	InputStr+=self.KeyToString("Sample")
	InputStr+=self.KeyToString("Sweep")
	self.Para["Seed"]=-int(random.random()*2**30)
	InputStr+=self.KeyToString("Seed")
	#InputStr+=self.KeyToString("ReadFile")
	InputStr+=self.KeyToString("Worm/Norm")
	InputStr+=self.KeyToString("Reweight")
	return InputStr

class JobConsistLoop(Job):
    def __init__(self, Para):
	Job.__init__(self, Para)
	self.KeepCPUBusy=True
	self.Para["Type: SCL"]=1

    def ToString(self,PID=0):
	InputStr=Job.ToString(self,PID)
	InputStr+=self.KeyToString("Type: SCL")
	InputStr+=self.KeyToString("ReadFile")
	return InputStr

class JobOutputLoop(Job):
    def __init__(self, Para):
	Job.__init__(self, Para)
	self.KeepCPUBusy=True
	self.Para["Type: OL"]=3

    def ToString(self,PID=0):
	InputStr=Job.ToString(self,PID)
	InputStr+=self.KeyToString("Type: OL")
	InputStr+=self.KeyToString("ReadFile")
	return InputStr

if __name__=="__main__":
    a=JobMonteCarlo({
	"__Execute": "./monte_carlo.exe",
	"__IsCluster":True,
	"__Duplicate":3,
	"IsForever" : True,
	"Sample" : 1000000,
	"Sweep" : 10,
	"Toss" : 1000,
	"IsLoad" : True,
	"Type" : 2,
	"Lx" :  4,
	"Ly" :  4,
	"Jcp" :  1.0,
	"Beta" :  0.9,
	"Order" :  2,
	"Reweight" : [1,5],
	#"ReadFile" : "0.90_1_coll",
	"Worm/Norm" : 0.5
    })
    print a.ToString(1)
