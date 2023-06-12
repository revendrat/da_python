from math import fsum

def average(x):
    return fsum(x)/float(len(x)) if x else 0

print("Average of numbers [0,0,3,1,4,1,5,9,0,0] :", average([0,0,3,1,4,1,5,9,0,0]))

print ("Average of numbers [1,2,3,4,5] :", average([1,2,3,4,5]))

