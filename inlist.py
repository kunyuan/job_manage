'''This is the input file of all jobs. 
   You have to add new job objects to TO_DO list
   if you want to run simulation.'''
import job_class as job
CPU = 4
SLEEP = 10   #check job status for every SLEEP seconds
TO_DO = []

# monte carlo job defintion
TO_DO.append(job.JobMonteCarlo({
    "__Execute" : "./monte_carlo.exe",
    "__Duplicate" : 3,
    "__IsCluster" : False,
    "__AutoRun" : True,
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
TO_DO.append(job.JobConsistLoop({   
    "__Execute" : ["python", "./run_self_consistent.py"],
    "__Duplicate" : 1,
    "__IsCluster" : False,
    "__AutoRun" : True,
    "IsLoad" : True,
    "Lx" :  4,
    "Ly" :  4,
    "Jcp" :  1.0,
    "Beta" :  0.9,
    "Order" :  1,
    "ReadFile" : "0.90_1_coll",
}))

# output loop job definition
TO_DO.append(job.JobOutputLoop({   
    "__Execute" : ["python", "./run_self_consistent.py"],
    "__Duplicate" : 1,
    "__IsCluster" : False,
    "__AutoRun" : False,
    "IsLoad" : True,
    "Lx" :  4,
    "Ly" :  4,
    "Jcp" :  1.0,
    "Beta" :  0.9,
    "Order" :  1,
    "ReadFile" : "0.90_1_coll",
}))

if __name__ == "__main__":
    for e in TO_DO:
        print e.ToString(1)+"\n"

