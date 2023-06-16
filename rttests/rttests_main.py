import pandas as pd
import numpy as np
import math

# from task import Task

__author__ = "Ziliang(Johnson)"
__copyright__ = "Copyright 2023, Ziliang(Johnson)"
__license__ = "MIT"
__maintainer__ = "Ziliang(Johnson)"
__email__ = "ziliang.zhang@email.ucr.edu"
__version__ = "1.0"

def rttests(taskset_path=None, test_type=None, sched_policy=None):
    if taskset_path is not None:
        print("taskset csv is located at:", taskset_path)
    else:
        raise FileNotFoundError("taskset_path NOT provided")
    if test_type is not None:
        print("Test type is:", test_type)
    else:
        raise ValueError("test_type NOT provided")
    if sched_policy is not None:
        print("Scheduling policy is:", sched_policy)
    else:
        raise ValueError("sched_policy NOT provided")
    
    df = pd.read_csv(taskset_path)
    df.dropna(inplace=True)

    if 'J' in df:
        print("WARNING: taskset has jitter!")
    
    if test_type == "rt":
        response_time_test(df, sched_policy)
    elif test_type == "ub":
        utilization_bound_test(df, sched_policy)
    else:
        raise ValueError("Invalid test_type")

def response_time_test(df: pd.DataFrame, sched_policy=None):
    R = 0 # worst case response time
    if sched_policy == "rm":
        df = df.sort_values(by=["T"], ignore_index=True)
    elif sched_policy == "dm":
        df = df.sort_values(by=["D"], ignore_index=True)
    else:
        raise ValueError("Invalid sched_policy")
    n = len(df.index) # number of tasks
    R = df["C"][n-1]
    iter = 0

    # import pdb; pdb.set_trace()
    if sched_policy == "rm":
        while True:
            R_new = df["C"][n-1]
            for j in range(n-1):
                if 'J' in df:
                    R_new += math.ceil((R + df["J"][j]) / df["T"][j]) * df["C"][j]
                else:
                    R_new += math.ceil(R / df["T"][j]) * df["C"][j]
            if 'J' in df:
                if R_new + df["J"][n-1]  > df["D"][n-1]:
                    print("Response time test failed!{} + {} > {}".format(R_new, df["J"][n-1], df["D"][n-1]))
                    break
                elif R_new == R:
                    print("Response time test passed!{} == {}".format(R_new, R))
                    break
            else:
                if R_new > df["D"][n-1]:
                    print("Response time test failed!{} > {}".format(R_new, df["D"][n-1]))
                    break
                elif R_new == R:
                    print("Response time test passed!{} == {}".format(R_new, R))
                    break
            R = R_new
            iter += 1
            print("{}th iteration R: {}".format(iter, R))
    if sched_policy == "dm":
        while True:
            R_new = df["C"][n-1]
            for j in range(n-1):
                if 'J' in df:
                    R_new += math.ceil((R + df["J"][j]) / df["D"][j]) * df["C"][j]
                else:
                    R_new += math.ceil(R / df["D"][j]) * df["C"][j]
            if 'J' in df:
                if R_new + df["J"][n-1]  > df["D"][n-1]:
                    print("Response time test failed!{} + {} > {}".format(R_new, df["J"][n-1], df["D"][n-1]))
                    break
                elif R_new == R:
                    print("Response time test passed!{} == {}".format(R_new, R))
                    break
            else:
                if R_new > df["D"][n-1]:
                    print("Response time test failed!{} > {}".format(R_new, df["D"][n-1]))
                    break
                elif R_new == R:
                    print("Response time test passed!{} == {}".format(R_new, R))
                    break
            R = R_new
            iter += 1
            print("{}th iteration R: {}".format(iter, R))

def utilization_bound_test(df: pd.DataFrame, sched_policy=None):
    n = len(df.index) # number of tasks
    utilization_bound = n * (math.pow(2, 1/n) - 1) # utilization bound
    utilization_T = 0
    utilization_D = 0
    for i in range(n):
        utilization_T += df["C"][i] / df["T"][i]
        utilization_D += df["C"][i] / df["D"][i]
    print("Utilization bound: {:.4f}".format(utilization_bound))
    print("Utilization (Period): {:.4f}".format(utilization_T))
    print("Utilization (Deadline): {:.4f}".format(utilization_D))

    if sched_policy == "rm":
        if utilization_T <= utilization_bound:
            print("Utilization bound test passed")
        elif utilization_T > utilization_bound and utilization_T <= 1:
            print("Utilization bound test inconclusive")
        else:
            print("Utilization bound test failed")
    elif sched_policy == "dm":
        if utilization_D <= utilization_bound:
            print("Utilization bound test passed")
        elif utilization_D > utilization_bound and utilization_D <= 1:
            print("Utilization bound test inconclusive")
        else:
            print("Utilization bound test failed")
    else:
        raise ValueError("Invalid sched_policy")

