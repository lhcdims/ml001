import numpy as np
import matplotlib.pyplot as plt
import math

# 输入结束
bolInputEnd = False

# 共有多少 点
intNumPoints = 0

# 输入的 x 和 y
strX = ''
strY = ''

# 输入的 x 和 y 转换成数字
intX = 0
intY = 0

# 储存所有输入
aryInput = []

while not bolInputEnd:
    strInput = input('请输入第 ' + str(intNumPoints) + ' 个坐标，[x,y]，按 q 结束：')
    intX = 0
    intY = 0
    strX = ''
    strY = ''
    if strInput == 'q':
        bolInputEnd = True
    elif (strInput.find('[') != 0):
        print('第一个字符应该是 [')
    elif (strInput.find(']') != len(strInput) - 1):
        print('最后一个字符应该是 ]')
    elif (strInput.find(',') == -1):
        print('中间应该有一个 ,')
    elif (strInput.find(',') <= strInput.find('[') + 1):
        print('[ 和 , 中间应该有一个数字')
    elif (strInput.find(']') <= strInput.find(',') + 1):
        print(', 和 ] 中间应该有一个数字')
    else:
        # 检查 ‘[’ 和 ‘,’ 中间，以及 ‘,’ 和 ‘]’ 中间，输入的是不是数字
        strX = strInput[strInput.find('[')+1:strInput.find(',')]
        strY = strInput[strInput.find(',')+1:strInput.find(']')]
        intX = float(strX)
        intY = float(strY)
        if math.isnan(intX):
            print('[ 和 , 中间应该是一个数字')
        elif math.isnan(intY):
            print(', 和 ] 中间应该是一个数字')
        else:
            # 查看数组内有没有重复
            bolFound = False
            for i in range(len(aryInput)):
                print(i)

print('输入结束了')

plt.plot([0,1],[0,1], 'blue')
plt.plot([0,1],[0,0], 'blue')
plt.plot([1,1],[0,1], 'blue')
plt.show()
