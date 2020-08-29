# In this Machine Learning Example, we try to use Gradient Descent
# to estimate the weight of a person y, with given height x of a person

intTotal = 0

# Define No. of Features of x
intN = 1

# Define Training Examples
aryT = []
aryT.append({'x': [20], 'y': 2})
aryT.append({'x': [40], 'y': 4})
aryT.append({'x': [60], 'y': 6})
aryT.append({'x': [120], 'y': 12})
aryT.append({'x': [160], 'y': 16})
aryT.append({'x': [162], 'y': 16.2})
aryT.append({'x': [171], 'y': 17.1})

# No. of Training Examples
intM = len(aryT)

# Learning Rate
intAlpha = 0.00001

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

intMaxTrainTimes = 10

# Init. Temp vars.
intSum = 0
intTemp = 0


# Iterates for intMaxTrainTimes
for j in range(intM):
  # Init Summation
  intSum = 0
  for t in range(intMaxTrainTimes):
    # Iterate for each feature
    for i in range(0, intN+1):
      intTemp = (aryTheta[0] + aryTheta[1] * aryT[j]['x'][0]) - aryT[j]['y']
      if i == 1:
        intTemp = intTemp * aryT[j]['x'][0]

    #   print('i: 0 | t: ' + str(t) + ' | j: ' + str(j) + ' | intTemp: ' + str(intTemp))
      intSum += intTemp
      intTotal += 1
    #End for

    # print('intSum: ' + str(intSum))

    # Calculate New Theta(0)
    aryTheta[i] = aryTheta[i] - intAlpha * intSum

    #print('i: 0 | aryTheta[0]: ' + str(aryTheta[0]))
    # print('aryTheta[0]: ' + str(aryTheta[0]))
    # print('aryTheta[1]: ' + str(aryTheta[1]))

# Print all Theta(s)
print('aryTheta[0]: ' + str(aryTheta[0]))
print('aryTheta[1]: ' + str(0.1 - aryTheta[1]))
print('intTotal: ' + str(intTotal))