# In this Machine Learning Example, we try to use Gradient Descent
# to estimate the weight of a person y, with given height x of a person

import math
import numpy as np 
from matplotlib import pyplot as plt

# Define No. of Features of x
intN = 3

intMaxTrainTimes = 10001

# Learning Rate
aryAlpha = []

for i in range(intN+1):
    aryAlpha.append(0.1 / math.pow(100000, i))

# Define Training Examples
aryT = []

aryT.append({'x': [0], 'y': 10.163})
aryT.append({'x': [60], 'y': 10.155})
aryT.append({'x': [120], 'y': 10.148})
aryT.append({'x': [180], 'y': 10.143})
aryT.append({'x': [240], 'y': 10.136})
aryT.append({'x': [300], 'y': 10.129})
aryT.append({'x': [360], 'y': 10.124})
aryT.append({'x': [420], 'y': 10.116})
aryT.append({'x': [480], 'y': 10.112})
aryT.append({'x': [540], 'y': 10.105})
aryT.append({'x': [600], 'y': 10.102})

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

# Init min step size
aryMinStepSize = []

for i in range(intM):
    aryMinStepSize.append(0)

# Init bolEnd
aryBolEnd = []

for i in range(0, intN+1):
    aryBolEnd.append(False)

bolTrainEnd = False

# Init check error
aryCheckError = [
    0,
    10000,
    20000,
    30000,
    40000,
    50000,
    60000,
    70000,
    80000,
    90000,
    100000,
]



# Iterates for intMaxTrainTimes
for t in range(intMaxTrainTimes):

    for i in range(len(aryCheckError)):
        if t == aryCheckError[i]:
            # Check Error and Print it out
            intSum = 0
            for m in range(intM):
                intTemp = 0
                for n in range(0, intN+1):
                    if n > 0:
                        intTemp += aryTheta[n] * math.pow(aryT[m]['x'][0], n)
                    else:
                        intTemp += aryTheta[n]
                intSum += math.pow(intTemp - aryT[m]['y'], 2)
            print("train times: " + str(t) + " , error: " + str(intSum))
    
    bolTrainEnd = True
    for i in range(0, intN+1):
        if aryBolEnd[i] == False:
            bolTrainEnd = False
            break
    
    if bolTrainEnd:
        break

    # Iterate for each feature
    for i in range(0, intN+1):
        if aryBolEnd[i] == False:
            # Init Summation
            intSum = 0

            for j in range(intM):
                intTemp = 0
                for n in range(0, intN+1):
                    if n > 0:
                        intTemp += aryTheta[n] * math.pow(aryT[j]['x'][0], n)
                    else:
                        intTemp += aryTheta[n]

                intTemp = intTemp - aryT[j]['y']

                if i > 0:
                    intTemp = intTemp * math.pow(aryT[j]['x'][0], i)

                intSum += intTemp
            #End for

            # Calculate New Theta(0)
            aryTheta[i] = aryTheta[i] - (1 / intM) * aryAlpha[i] * intSum

            if abs((1 / intM) * aryAlpha[i] * intSum) < aryMinStepSize[i]:
                aryBolEnd[i] = True



# Print all Theta(s)
for i in range(0,intN+1):
    print('aryTheta[' + str(i) + ']: ' + str(aryTheta[i]))



# Plot graph
aryX = []
aryY = []
aryH = []

for i in range(intM):
    #plt.plot(aryT[i]['x'][0], aryT[i]['y'], 'bo')
    intTemp = 0
    for j in range(0, intN+1):
        if j > 0:
            intTemp += aryTheta[j] * math.pow(aryT[i]['x'][0], j)
        else:
            intTemp += aryTheta[j]
    aryX.append(aryT[i]['x'][0])
    aryY.append(aryT[i]['y'])
    aryH.append(intTemp)

plt.plot(aryX, aryY, 'bx')
plt.plot(aryX, aryH, 'g')
plt.show()