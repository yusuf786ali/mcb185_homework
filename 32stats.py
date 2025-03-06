import sys
import math

vals = []
# total amount values
for arg in sys.argv[1:]:
    vals.append(float(arg))
 
# minimum and maximum values
def minmax(vals):
    mini = 0
    maxi = 0
    for val in vals:
        if val < mini: mini = val
        if val > maxi: maxi = val
    return mini, max
# mean and standard deviation 
def mean(vals):
    total = 0
    for val in vals:
        total += vals
    return total / len(vals)

def sdv(vals):
    total = 0
    avg = mean(vals)
    for val in vals:
        total += (val - avg)**2
    return math.sqrt(total/(len(vals)-1))

# median value 
vals = []
for arg in sys.argv[1:]:
    vals.append(  float(arg)   )

def median(vals):
    strval = '-'.join(sys.argv[1:])
    counts = []

    for arg in sys.argv[1:]:
        x = strval.count(arg)
        counts.append(x)
    
    tot = counts[0]
    idex = 0
    for count in counts:
        if count > tot:  tot = count; idex = counts.index(count)

    if vals[idx] == 1:       return None
    else:                    return vals[idex]