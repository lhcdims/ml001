# In this Machine Learning Example, we try to use Locally Weighted Regression
# to estimate the weight of a person y, with given height x of a person

import math

# Define No. of Features of x
intN = 1

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

# Learning Rate
intAlpha = 0.0001

# Init Array Parameters
aryTheta = []
for i in range(intN+1):
  if (i == 0):
    # Init. Theta0 with 0
    aryTheta.append(0)
  else:
    # Init. Theta1 with 0
    aryTheta.append(0)


# Hypothesis H, t stands for theta
# H(t) = t0 x0 + t1 x1

intMaxTrainTimes = 1000


# Init. Temp vars.
intSum = 0
intTemp = 0


# Define bandwidth Tau
intTau = 5

# Define Target X
intXTarget = 110

# Calculate w(j) for each x(j)
aryOmega = []
for j in range(intM):
  intTemp = math.exp((-1 * math.pow(aryT[j]['x'][0] - intXTarget, 2)) / (2 * math.pow(intTau, 2)))
  aryOmega.append(intTemp)
  #print(intTemp)

# Iterates for intMaxTrainTimes
for t in range(intMaxTrainTimes):
  # Iterate for each feature
  for i in range(0, intN+1):
    # Init Summation
    intSum = 0

    for j in range(intM):
      intTemp = ((aryTheta[0] + aryTheta[1] * aryT[j]['x'][0]) - aryT[j]['y'])
      if i > 0:
        intTemp = intTemp * aryT[j]['x'][i-1]

      intTemp = intTemp * aryOmega[j]

      intSum += intTemp
    #End for

    # Calculate New Theta(0)
    aryTheta[i] = aryTheta[i] - intAlpha * intSum

# Print all Theta(s)
print('aryTheta[0]: ' + str(aryTheta[0]))
print('aryTheta[1]: ' + str(aryTheta[1]))

# Calculate Target Y
intY = aryTheta[0] + intXTarget * aryTheta[1]

# Print Target Y:
print('Target Y: ' + str(intY))
