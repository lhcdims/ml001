# Array which stores ALL path distances
aryData = [
    # X0
    [
        0,
        94,
        76,
        141,
        91,
        60,
        120,
        145,
        91,
        74,
        90,
        55,
        145,
        108,
        41,
        49,
        33,
        151,
        69,
        111,
        24,
    ],
    # A1
    [
        94,
        0,
        156,
        231,
        64,
        93,
        108,
        68,
        37,
        150,
        130,
        57,
        233,
        26,
        62,
        140,
        61,
        229,
        120,
        57,
        109,
    ],
    # B2
    [
        76,
        156,
        0,
        80,
        167,
        133,
        124,
        216,
        137,
        114,
        154,
        100,
        141,
        161,
        116,
        37,
        100,
        169,
        49,
        185,
        84,
    ],
    # C3
    [
        141,
        231,
        80,
        0,
        229,
        185,
        201,
        286,
        216,
        139,
        192,
        178,
        113,
        239,
        182,
        92,
        171,
        155,
        128,
        251,
        137,
    ],
    # D4
    [
        91,
        64,
        167,
        229,
        0,
        49,
        163,
        65,
        96,
        114,
        76,
        93,
        200,
        91,
        51,
        139,
        72,
        185,
        148,
        26,
        92,
    ],
    # E5
    [
        60,
        93,
        133,
        185,
        49,
        0,
        165,
        115,
        112,
        65,
        39,
        91,
        151,
        117,
        39,
        99,
        61,
        139,
        128,
        75,
        49,
    ],
    # F6
    [
        120,
        108,
        124,
        201,
        163,
        165,
        0,
        173,
        71,
        194,
        203,
        74,
        254,
        90,
        127,
        136,
        104,
        269,
        75,
        163,
        144,
    ],
    # G7
    [
        145,
        68,
        216,
        286,
        65,
        115,
        173,
        0,
        103,
        179,
        139,
        123,
        265,
        83,
        104,
        194,
        116,
        250,
        186,
        39,
        152,
    ],
    # H8
    [
        91,
        37,
        137,
        216,
        96,
        112,
        71,
        103,
        0,
        160,
        151,
        39,
        236,
        25,
        75,
        130,
        61,
        239,
        95,
        93,
        112,
    ],
    # I9
    [
        74,
        150,
        114,
        139,
        114,
        65,
        194,
        179,
        160,
        0,
        54,
        127,
        86,
        171,
        89,
        77,
        99,
        80,
        134,
        140,
        50,
    ],
    # J10
    [
        90,
        130,
        154,
        192,
        76,
        39,
        203,
        139,
        151,
        54,
        0,
        129,
        133,
        155,
        78,
        117,
        99,
        111,
        159,
        101,
        71,
    ],
    # K11
    [
        55,
        57,
        100,
        178,
        93,
        91,
        74,
        123,
        39,
        127,
        129,
        0,
        199,
        61,
        53,
        91,
        30,
        206,
        63,
        101,
        78,
    ],
    # L12
    [
        145,
        233,
        141,
        113,
        200,
        151,
        254,
        265,
        236,
        86,
        133,
        199,
        0,
        251,
        171,
        118,
        176,
        46,
        182,
        226,
        125,
    ],
    # M13
    [
        108,
        26,
        161,
        239,
        91,
        117,
        90,
        83,
        25,
        171,
        155,
        61,
        251,
        0,
        83,
        151,
        75,
        251,
        119,
        81,
        127,
    ],
    # N14
    [
        41,
        62,
        116,
        182,
        51,
        39,
        127,
        104,
        75,
        89,
        78,
        53,
        171,
        83,
        0,
        90,
        24,
        168,
        99,
        69,
        49,
    ],
    # O15
    [
        49,
        140,
        37,
        92,
        139,
        99,
        136,
        194,
        130,
        77,
        117,
        91,
        118,
        151,
        90,
        0,
        80,
        139,
        65,
        159,
        50,
    ],
    # P16
    [
        33,
        61,
        100,
        171,
        72,
        61,
        104,
        116,
        61,
        99,
        99,
        30,
        176,
        75,
        24,
        80,
        0,
        179,
        76,
        86,
        52,
    ],
    # Q17
    [
        151,
        229,
        169,
        155,
        185,
        139,
        269,
        250,
        239,
        80,
        111,
        206,
        46,
        251,
        168,
        139,
        179,
        0,
        202,
        211,
        128,
    ],
    # R18
    [
        69,
        120,
        49,
        128,
        148,
        128,
        75,
        186,
        95,
        134,
        159,
        63,
        182,
        119,
        99,
        65,
        76,
        202,
        0,
        161,
        90,
    ],
    # S19
    [
        111,
        57,
        185,
        251,
        26,
        75,
        163,
        39,
        93,
        140,
        101,
        101,
        226,
        81,
        69,
        159,
        86,
        211,
        161,
        0,
        115,
    ],
    # T20
    [
        24,
        109,
        84,
        137,
        92,
        49,
        144,
        152,
        112,
        50,
        71,
        78,
        125,
        127,
        49,
        50,
        52,
        128,
        90,
        115,
        0,
    ],
]

# Variables

import random
import numpy as np

N_SIZE = 21             # no. of cities
POP_SIZE = 100          # population size
N_GENERATIONS = 40000   # no. of iterations

pop = []
dis = []
selectIndex = []
child = []
childDis = 99999

# Methods

def calDisChild(aryChild):
    global pop, dis

    intTemp = 0
    for j in range(N_SIZE-1):
        intTemp += aryData[aryChild[j]][aryChild[j+1]]
    intTemp += aryData[aryChild[N_SIZE-1]][aryChild[0]]
    return intTemp

def initDis():
    global pop, dis

    for i in range(POP_SIZE):
        intTemp = 0
        for j in range(N_SIZE-1):
            intTemp += aryData[pop[i][j]][pop[i][j+1]]
        intTemp += aryData[pop[i][N_SIZE-1]][pop[i][0]]
        dis.append(intTemp)

def init():
    global pop, dis

    aryTemp = []
    for j in range(N_SIZE):
        aryTemp.append(j)

    i = 0
    while i < POP_SIZE:
        i += 1
        pop.append(random.sample(aryTemp, N_SIZE))

def evaluate():
    global pop, dis

    bolFound = False

    for i in range(POP_SIZE):
        if (pop[i] == child):
            bolFound = True
            break

    if (childDis < max(dis) and not bolFound):
        pop[dis.index(max(dis))] = child
        dis[dis.index(max(dis))] = childDis

def select():
    global pop, dis

    aryZipped = list(zip(dis, pop))

    # Asc order sort
    aryResult = sorted(aryZipped)

    aryResult2 = list(zip(*aryResult))

    pop = list(aryResult2[1])
    dis = list(aryResult2[0])

    # Desc order sort
    disReverse = sorted(dis, reverse=True)

    intP = np.sum(dis)
    aryP = []

    for i in range(POP_SIZE):
        aryP.append(disReverse[i] / intP)

    return np.random.choice(POP_SIZE, 2, p=aryP)

def crossover():
    global pop, dis

    # Init
    intNSize = int(N_SIZE)
    intNSizeD2 = int(11)

    # Partially mapped crossover (PMX)
    intRandom = random.randint(0, intNSizeD2)

    # Get random section of first selected array
    firstPart = pop[selectIndex[0]][intRandom:intRandom+intNSize-intNSizeD2]

    # Vars for loop
    arySecondFirst = []
    arySecondSecond = []
    bolIndexLargerThanRandom = False
    intLastIndex = 0

    # Loop to add cities from second selected array which are
    # Not appeared in the random section
    # Not repeating in already added cities from second selected array
    for i in range(intNSizeD2):
        # Check before or after the random section
        if (i >= intRandom):
            bolIndexLargerThanRandom = True

        # loop
        for x in range(intLastIndex, intNSize):
            bolFound = False
            for y in range(intNSize-intNSizeD2):
                if (pop[selectIndex[1]][x] == firstPart[y]):
                    bolFound = True
                    break
            if not bolFound:
                if not bolIndexLargerThanRandom:
                    arySecondFirst.append(pop[selectIndex[1]][x])
                else:
                    arySecondSecond.append(pop[selectIndex[1]][x])
                intLastIndex = x+1
                break

    # Add up arrays to form new child
    child = arySecondFirst + firstPart + arySecondSecond

    return child

def mutate():
    global pop, dis, child

    childTemp = child

    bolEnd = False
    while not bolEnd:
        intA = random.randint(0,N_SIZE-1)
        intB = random.randint(0,N_SIZE-1)
        if (intA != intB):
            bolEnd = True

    intTemp = childTemp[intA]
    childTemp[intA] = childTemp[intB]
    childTemp[intB] = intTemp

    if calDisChild(childTemp) < calDisChild(child):
        child = childTemp

def formatPop(aryPop):
    index = aryPop.index(0)

    aryFirst = aryPop[index:]
    arySecond = aryPop[:index]

    aryResult = aryFirst + arySecond

    for i in range(1, 21):
        aryResult[i] = chr(aryResult[i]+64)

    aryResult[0] = "X"
    aryResult.append("X")
    return aryResult

# Main Program

# Init
init()
initDis()

# Output Init Result
print("")
print("Start")
print("Min: " + str(min(dis)))
print("Max: " + str(max(dis)))
print("")

# Iterate for N generations
for i in range(N_GENERATIONS):
    # Discriminate the worst person
    evaluate()

    # Select 2 parents
    selectIndex = select()

    # Create child
    child = crossover()

    # A small chance for child to mutate
    mutate()

    # Calculate child's performance
    childDis = calDisChild(child)

# Output Iteration Result
print("End")
print("Min: " + str(min(dis)))
print("Max: " + str(max(dis)))
print("")
print("Minimum distance path: " + str(min(dis)))
print(formatPop(pop[dis.index(min(dis))]))
print("")