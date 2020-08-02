# In this NON-Machine Learning Example, we try to use a simple program
# to determine whether the no. of 1 in the upper part of the array
# is more than the no. of 1 in the lower part of the array

# Define Array
aryT = []
aryT.append([1,1,0,0,0,1,0,0])
aryT.append([0,1,0,1,0,1,0,0])
aryT.append([0,0,1,0,0,1,0,0])
aryT.append([0,0,0,0,0,0,0,1])
aryT.append([0,0,0,0,0,1,0,0])
aryT.append([1,0,1,0,0,0,0,0])
aryT.append([0,0,0,0,0,0,0,0])
aryT.append([0,0,1,0,0,1,0,0])

# No. of Rows and Columns
intM = len(aryT)
intN = len(aryT[0])

# Init No. of Up and Down
intUp = 0
intDown = 0

# Count No. of Up and Down in Array
for i in range(intM):
    for j in range(intN):
        if (i <= 3):
            if (aryT[i][j] == 1):
                intUp += 1
        else:
            if (aryT[i][j] == 1):
                intDown += 1


# Print result
print('intUp: ' + str(intUp))
print('intDown: ' + str(intDown))

if (intUp >= intDown):
    print('The result is: 1')
else:
    print('The result is: 0')