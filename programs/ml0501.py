# In this Machine Learning Example, we try to use Gradient Descent
# to draw a curve, with given weights and heights of people

import math
from matplotlib import pyplot as plt

# Define No. of Features of x
intN = 3

# Define Learning Rate
aryAlpha = [
    0.1,
    0.00001,
    0.000000001,
    0.0000000000001,
]

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
aryTheta = [
    0,
    0,
    0,
    0,
]

# Init maximum training times
intMaxTrainTimes = 10000



# Iterates for intMaxTrainTimes
for t in range(intMaxTrainTimes):

    # Iterate for each feature
    for i in range(0, intN+1):
        # Init Summation
        intSum = 0

        # Iterate for each training example
        for j in range(intM):

            # Init temp for calculation
            intTemp = 0

            # Sum up to get predicted value of the hypothesis
            for n in range(0, intN+1):
                if n > 0:
                    intTemp += aryTheta[n] * math.pow(aryT[j]['x'][0], n)
                else:
                    intTemp += aryTheta[n]

            # Calculate Error
            intTemp = intTemp - aryT[j]['y']

            if i > 0:
                intTemp = intTemp * math.pow(aryT[j]['x'][0], i)

            intSum += intTemp
        #End for

        # Calculate New Theta(0)
        aryTheta[i] = aryTheta[i] - (1 / intM) * aryAlpha[i] * intSum



# Print all Theta(s)
print('aryTheta[0]: ' + str(aryTheta[0]))
print('aryTheta[1]: ' + str(aryTheta[1]))
print('aryTheta[2]: ' + str(aryTheta[2]))
print('aryTheta[3]: ' + str(aryTheta[3]))



# Check Error
intSum = 0
aryTheta = [
    0.292563,
    0.089824,
    0.000057,
    0.000010,
]
for m in range(intM):
    intTemp = 0
    for n in range(0, intN+1):
        if n > 0:
            intTemp += aryTheta[n] * math.pow(aryT[m]['x'][0], n)
        else:
            intTemp += aryTheta[n]
    intSum += math.pow(intTemp - aryT[m]['y'], 2)
print("Error: " + str(intSum))



# Plot graph
aryX = []
aryY = []
aryH = []
for i in range(intM):
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