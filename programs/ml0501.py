# In this Machine Learning Example, we try to use Gradient Descent
# to estimate the weight of a person y, with given height x of a person

import math
import numpy as np 
from matplotlib import pyplot as plt 

# Define No. of Features of x
intN = 1

intMaxTrainTimes = 50000

# Learning Rate
intAlpha = 0.00001
#intAlpha = 0.00000000000001

# Define Training Examples
aryT = []
aryT.append({'x': [10], 'y': 0.5})
aryT.append({'x': [20], 'y': 1.5})
aryT.append({'x': [40], 'y': 3.5})
aryT.append({'x': [60], 'y': 8})
aryT.append({'x': [80], 'y': 12})
aryT.append({'x': [100], 'y': 20})
aryT.append({'x': [120], 'y': 30})
aryT.append({'x': [140], 'y': 40})
aryT.append({'x': [160], 'y': 55})
aryT.append({'x': [170], 'y': 70})
aryT.append({'x': [180], 'y': 76})

# No. of Training Examples
intM = len(aryT)

# Init Array Parameters
aryTheta = []

for i in range(0, intN+1):
    if i > 0:
        aryTheta.append(0)
    else:
        aryTheta.append(0)

# Init. Temp vars.
intSum = 0

# Iterates for intMaxTrainTimes
for t in range(intMaxTrainTimes):

    # Iterate for each feature
    for i in range(0, intN+1):
        # Init Summation
        intSum = 0

        for j in range(intM):
            for n in range(0, intN+1):
                if n > 0:
                    intTemp += aryTheta[n] * math.pow(aryT[j]['x'][0], n)
                else:
                    intTemp = aryTheta[n]
            intTemp = intTemp - aryT[j]['y']

            if i > 0:
                intTemp = intTemp * math.pow(aryT[j]['x'][0], n)

            intSum += intTemp
        #End for

        # Calculate New Theta(0)
        aryTheta[i] = aryTheta[i] - intAlpha * intSum


# Print all Theta(s)
for i in range(0,intN+1):
    print('aryTheta[' + str(i) + ']: ' + str(aryTheta[i]))

for i in range(intM):
    plt.plot(aryT[i]['x'][0], aryT[i]['y'], 'bo')
    intTemp = 0
    for j in range(0, intN+1):
        if j > 0:
            intTemp += aryTheta[j] * math.pow(aryT[i]['x'][0], j)
        else:
            intTemp += aryTheta[j]
    plt.plot(aryT[i]['x'][0], intTemp, 'go')

aryTest = []
for i in range(0, len(aryTest)):
    intTemp = 0
    for j in range(0, intN+1):
        if j > 0:
            intTemp += aryTheta[j] * math.pow(aryTest[i], j)
        else:
            intTemp += aryTheta[j]
    plt.plot(aryTest[i], intTemp, 'go')

plt.show()