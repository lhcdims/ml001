# In this Machine Learning Example, we try to use Logistic Regression
# to distinguish numeric digits shown in a 8 x 8 LED panel

import math

# Define No. of Features of x
intN = 64

# Define Training Examples
aryT = []

intNumOfDigits = 3

# 0
aryT.append({'x': [
0, 0, 1, 1, 1, 1, 0, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 0, 1, 1, 1, 1, 0, 0,
], 'y': 0})
aryT.append({'x': [
0, 1, 1, 1, 1, 1, 1, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 1, 1, 1, 1, 1, 1, 0,
], 'y': 0})
aryT.append({'x': [
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
], 'y': 0})
aryT.append({'x': [
0, 0, 1, 1, 1, 1, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 0, 0, 1, 0, 0,
0, 0, 1, 1, 1, 1, 0, 0,
], 'y': 0})

# 1
aryT.append({'x': [
0, 0, 0, 1, 0, 0, 0, 0,
0, 0, 0, 1, 0, 0, 0, 0,
0, 0, 0, 1, 0, 0, 0, 0,
0, 0, 0, 1, 0, 0, 0, 0,
0, 0, 0, 1, 0, 0, 0, 0,
0, 0, 0, 1, 0, 0, 0, 0,
0, 0, 0, 1, 0, 0, 0, 0,
0, 0, 0, 1, 0, 0, 0, 0,
], 'y': 1})
aryT.append({'x': [
0, 0, 0, 0, 1, 0, 0, 0,
0, 0, 0, 0, 1, 0, 0, 0,
0, 0, 0, 0, 1, 0, 0, 0,
0, 0, 0, 0, 1, 0, 0, 0,
0, 0, 0, 0, 1, 0, 0, 0,
0, 0, 0, 0, 1, 0, 0, 0,
0, 0, 0, 0, 1, 0, 0, 0,
0, 0, 0, 0, 1, 0, 0, 0,
], 'y': 1})
aryT.append({'x': [
0, 0, 1, 0, 0, 0, 0, 0,
0, 0, 1, 0, 0, 0, 0, 0,
0, 0, 1, 0, 0, 0, 0, 0,
0, 0, 1, 0, 0, 0, 0, 0,
0, 0, 1, 0, 0, 0, 0, 0,
0, 0, 1, 0, 0, 0, 0, 0,
0, 0, 1, 0, 0, 0, 0, 0,
0, 0, 1, 0, 0, 0, 0, 0,
], 'y': 1})
aryT.append({'x': [
0, 0, 0, 0, 0, 1, 0, 0,
0, 0, 0, 0, 0, 1, 0, 0,
0, 0, 0, 0, 0, 1, 0, 0,
0, 0, 0, 0, 0, 1, 0, 0,
0, 0, 0, 0, 0, 1, 0, 0,
0, 0, 0, 0, 0, 1, 0, 0,
0, 0, 0, 0, 0, 1, 0, 0,
0, 0, 0, 0, 0, 1, 0, 0,
], 'y': 1})
aryT.append({'x': [
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
], 'y': 1})
aryT.append({'x': [
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 1, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
0, 0, 0, 1, 1, 0, 0, 0,
0, 1, 1, 1, 1, 1, 1, 0,
], 'y': 1})
aryT.append({'x': [
0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
], 'y': 1})
aryT.append({'x': [
0, 0, 1, 1, 0, 0, 0, 0,
0, 1, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
1, 1, 1, 1, 1, 1, 0, 0,
], 'y': 1})
aryT.append({'x': [
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
], 'y': 1})
aryT.append({'x': [
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 1, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 1, 1, 1, 1, 1, 1,
], 'y': 1})

# 2
aryT.append({'x': [
0, 0, 1, 1, 1, 1, 0, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 0, 0, 0, 0, 0, 1, 0,
0, 0, 0, 0, 1, 1, 0, 0,
0, 0, 1, 1, 0, 0, 0, 0,
0, 1, 0, 0, 0, 0, 0, 0,
0, 1, 0, 0, 0, 0, 1, 0,
0, 0, 1, 1, 1, 1, 0, 0,
], 'y': 2})
# 2
aryT.append({'x': [
0, 0, 1, 1, 1, 1, 0, 0,
0, 0, 0, 0, 0, 1, 0, 0,
0, 0, 0, 0, 0, 1, 0, 0,
0, 0, 1, 1, 1, 1, 0, 0,
0, 0, 1, 0, 0, 0, 0, 0,
0, 0, 1, 0, 0, 0, 0, 0,
0, 0, 1, 0, 0, 0, 0, 0,
0, 0, 1, 1, 1, 1, 0, 0,
], 'y': 2})




# No. of Training Examples
intM = len(aryT)

# Learning Rate
intAlpha = 0.1

# Init Array Parameters
aryTheta = []
for i in range(0, intNumOfDigits):
    aryTheta.append([
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    ])

# Hypothesis H, t stands for theta
# G(x) = t0 x0 + t1 x1 + ... + 
# H(z) = 1 / (1 + e^(-z))

intTrainTimes = 100

# Iterates for Each Digits
for u in range(intNumOfDigits):
    # Iterates for intTrainTimes
    for t in range(intTrainTimes):

        # Iterates for each feature
        for i in range(intN):

            # Sum of error between Y and Hypothesis
            intSum = 0

            # Iterates for each training example
            for j in range(intM):

                intTemp1 = 0
                intTemp2 = 0

                # Sum up to get Theta transposed X
                for z in range(intN):
                    intTemp1 += aryTheta[u][z] * aryT[j]['x'][z]

                # Error between Y and Hypothesis in jth training example

                # Get Y
                intTempY = 0
                if (u == aryT[j]['y']):
                    intTempY = 1
                else:
                    intTempY = 0

                intTemp2 = intTempY - (1 / (1 + math.exp(-intTemp1)))
                intTemp2 = intTemp2 * aryT[j]['x'][i]
                intSum += intTemp2
            
            # Update Theta i
            aryTheta[u][i] = aryTheta[u][i] + intAlpha * intSum

# Print all Theta(s)
# print('aryTheta: ' + str(aryTheta))

# Testing

# Array which stores testing values
aryTest = [
    0, 0, 0, 1, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 0, 0, 0,
    0, 0, 0, 1, 1, 0, 0, 0,
    0, 0, 0, 1, 1, 0, 0, 0,
    0, 0, 0, 1, 1, 0, 0, 0,
    0, 0, 0, 1, 1, 0, 0, 0,
    0, 0, 0, 1, 1, 0, 0, 0,
    0, 0, 0, 1, 1, 0, 0, 0,
]

intTemp1 = 0
aryAnswer = []
intAnswer = 0
intU = 0

for u in range(0, intNumOfDigits):
    intTemp1 = 0
    for i in range(0, intN):
        intTemp1 += aryTheta[u][i] * aryTest[i]

    # The output of the hypothesis
    aryAnswer.append(1 / (1 + math.exp(-intTemp1)))

    # Print the output given by the hypothesis
    print("Probability of Getting " + str(u) + " : " + str(aryAnswer[u]))

    if (aryAnswer[u] > intAnswer):
        intAnswer = aryAnswer[u]
        intU = u

print('I guess the Answer is: ' + str(intU))
