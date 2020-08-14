# In this Machine Learning Example, we try to use Gradient Descent
# to predict if there are more upper or lower points

import math

# Define No. of Features of x
intN = 64

# Define Training Examples
aryT = []
aryT.append({'x': [
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
], 'y': 1})
aryT.append({'x': [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
], 'y': 0})


# No. of Training Examples
intM = len(aryT)

# Learning Rate
intAlpha = 0.1

# Init Array Parameters
aryTheta = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
]

# Hypothesis H, t stands for theta
# G(x) = t0 x0 + t1 x1 + ... + 
# H(z) = 1 / (1 + e^(-z))

intTrainTimes = 100

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
                intTemp1 += aryTheta[z] * aryT[j]['x'][z]

            # Error between Y and Hypothesis in jth training example
            intTemp2 = aryT[j]['y'] - (1 / (1 + math.exp(-intTemp1)))
            intTemp2 = intTemp2 * aryT[j]['x'][i]
            intSum += intTemp2
        
        # Update Theta i
        aryTheta[i] = aryTheta[i] + intAlpha * intSum

# Print all Theta(s)
print('aryTheta: ' + str(aryTheta))

# Testing

# Array which stores testing values
aryTest = [
    0, 1, 0, 0, 1, 0, 1, 1,
    0, 1, 0, 1, 0, 1, 1, 1,
    1, 1, 1, 0, 1, 0, 1, 1,
    0, 0, 0, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 1, 0, 0, 0, 1, 0, 0,
]

intTemp1 = 0

for i in range(0, intN):
    intTemp1 += aryTheta[i] * aryTest[i]

# The output of the hypothesis
intAnswer = 1 / (1 + math.exp(-intTemp1))

# Print the output given by the hypothesis
print("Test Answer: " + str(intAnswer))