#Please define your job dictionary here
from job_class import *
cpu=4
ToDo=[]

# monte carlo job defintion
ToDo.append(JobMonteCarlo({   
    "__Execute" : "./monte_carlo.exe",
    "__Duplicate" : 3,
    "__IsCluster" : False,
    "IsForever" : True,
    "Sample" : 1000000,
    "Sweep" : 10,
    "Toss" : 1000,
    "IsLoad" : True,
    "Lx" :  4,
    "Ly" :  4,
    "Jcp" :  1.0,
    "Beta" :  0.9,
    "Order" :  1,
    "Reweight" : [1],
    #"ReadFile" : "0.90_1_coll",
    "Worm/Norm" : 0.5 
}))

# self consist loop job definition
ToDo.append(JobConsistLoop({   
    "__Execute" : "./run_self_consistent.py",
    "__Duplicate" : 1,
    "__IsCluster" : False,
    "IsLoad" : True,
    "Lx" :  4,
    "Ly" :  4,
    "Jcp" :  1.0,
    "Beta" :  0.9,
    "Order" :  1,
    "ReadFile" : "0.90_1_coll",
}))

# output loop job definition
ToDo.append(JobOutputLoop({   
    "__Execute" : "./run_self_consistent.py",
    "__Duplicate" : 1,
    "__IsCluster" : False,
    "IsLoad" : True,
    "Lx" :  4,
    "Ly" :  4,
    "Jcp" :  1.0,
    "Beta" :  0.9,
    "Order" :  1,
    "ReadFile" : "0.90_1_coll",
}))

if __name__=="__main__":
    for e in ToDo:
	print e.ToString(1)+"\n"

