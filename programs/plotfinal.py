import matplotlib.pyplot as plt
import math
import itertools

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


# 各功能定义

# 本功能看看 3 点是不是在一条线上，如果是，不允许画图
def judge_three_point_in_one_line(pos):
    if pos[0][0] - pos[1][0] == 0:
        intMAB = 'infinity'
    else:
        intMAB = (pos[0][1] - pos[1][1]) / (pos[0][0] - pos[1][0])
    if pos[1][0] - pos[2][0] == 0:
        intMBC = 'infinity'
    else:
        intMBC = (pos[1][1] - pos[2][1]) / (pos[1][0] - pos[2][0])

    if intMAB == intMBC:
        return True
    else:
        return False

# 本功能判断有没有任何三个点在同一条线上
def judge_points_in_one_line(pos):
    # 首先判断 pos的个数是否大于三个，小于3个点情况返回False
    if len(pos) < 3:
        return False
    # 使用三重循环的形式， 一个个遍历所有的点， 
    # 开始第一重遍历， 从第一个遍历到倒数第三个点
    for x in range(0, len(pos)-2):
        # 开始第二重遍历， 从第一重遍历的下一个点开始遍历 到 倒数第二个点
        for y in range(x+1, len(pos)-1):
            # 开始第三重遍历， 从第二重遍历的下一个点开始遍历 到 倒数第一个点
            for z in range(y+1, len(pos)):
                # 取出三重遍历的这三个点， 使用judge_three_point_in_one_line 判断是否共线， 共线的情况 print 共线的点数，并返回 True
                bolSameLine = judge_three_point_in_one_line([pos[x], pos[y], pos[z]])
                if bolSameLine:
                    print(str(pos[x]) + ", " + str(pos[y]) + ", " + str(pos[z]))
                    return True
    return False

# 本功能计算两点之间的距离
def distance_between_two_point(pos1, pos2):
    #返回 sqrt((x1-x2)**2 + (y1-y2)**2)
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)


# 计算所有点的距离
def distance_points(pos, order):
    
    distance = 0.0
    #使用循环，先从order的第1个点到order的倒数第2个点， 再加上order的倒数第1个点到order的第1个点的距离

    #循环到倒数第2个点
    for i in range(0, len(pos)-1):
        #distance 加上 当前点到order的下一个点的距离， 使用distance_between_two_point计算距离
        distance += distance_between_two_point(pos[order[i]], pos[order[i+1]])
    
    #distance加上order的最后一个点到order的第一个点的距离
    distance += distance_between_two_point(pos[order[len(pos)-1]], pos[order[0]])
    
    return distance

# 这个没搞懂，用了别的方法
# def get_pos_order(pos):
#     pos_order = [0,1,2]
#     #判断点的个数大于2个，即至少3个点
#     if len(pos) < 3:
#         return 0

#     #前三个点构成三角形， 之后一个个点插入，每插入一个点都是寻找使得总距离最小的排序
    
#     #从第4点来开始插入，到最后一个点为止
#     for x in range(3, len(pos)):
#         #再开始一个循环，在已有顺序的间隔处都计算一次总距离，保存最小距离的排序
#         #声明一个临时最小距离变量并赋值无限大 min_dis = np.inf
#         min_dis = np.inf
#         #申明一个空的临时顺序列表
#         temp_order = []
#         #从0开始，到已有点的个数为止
#         for y in range(0, x+1):
#             #临时列表复制成当前的顺序列表 pos_order
#             temp_order = pos_order
#             #在临时列表中插入新加的点
#             temp_order.append(x)
#             #计算总距离， 使用distance_points
#             intDis = distance_points(pos, temp_order)
#             #判断总距离是不是小于临时最小距离变量
#             if intDis < min_dis:
#                 #总距离是小于的场合，更新最小距离变量和当前
#                 min_dis = intDis
#         #小循环结束，新加入的点找到对应最小距离的顺序
        
    
#     #大循环结束，返回最后的顺序
#     return pos_order


#while bolInputEnd:
while not bolInputEnd:
    strInput = input('请输入第 ' + str(intNumPoints+1) + ' 个坐标，[x,y]，按 q 结束：')
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
        bolWithError = False
        try:
            intX = float(strX)
            intY = float(strY)
        except:
            bolWithError = True
        if bolWithError:
            print('只能输入数字')
        else:
            # 查看数组内有没有重复
            bolFound = False
            for i in range(len(aryInput)):
                if (aryInput[i][0] == intX and aryInput[i][1] == intY):
                    bolFound = True
                    print('您已经输入过这个点了：' + strInput)
            
            if (not bolFound):
                aryInput.append([intX, intY])
                intNumPoints += 1

print('输入结束了, 计算中，请稍后（计算时间可能长达数十秒）')

# 测试用輸入
# aryInput.append([0,0])
# aryInput.append([1,0])
# aryInput.append([1,1])
# aryInput.append([0,1])
# aryInput.append([0.5,0.6])
# aryInput.append([0.1,0.3])
# aryInput.append([0.9,0.8])
# intNumPoints = len(aryInput)

bolOK = False

if intNumPoints < 3:
    print('不能少于三个点，程序结束')
else:
    if judge_points_in_one_line(aryInput):
        print('不能出现连在一条线上的三个点，程序结束')
    else:
        bolOK = True

if bolOK:
    # 创建数组列举所有可能性
    aryOrder = []
    # 创建数组记录每一种可能性的距离
    aryDis = []
    
    aryTemp = []
    for i in range(0, intNumPoints):
        aryTemp.append(i)

    aryOrder = list(itertools.permutations(aryTemp))

    for i in range(0, len(aryOrder)):
        # 计算每种可能性的长度
        aryDis.append(distance_points(aryInput, aryOrder[i]))

    zipped_lists = zip(aryDis, aryOrder)
    sorted_pairs = sorted(zipped_lists)

    temp_lists = zip(*sorted_pairs)
    aryDis, aryOrder = [ list(temp) for temp in  temp_lists]

    # 长度排序后，最短路径在数组第一条
    aryActualOrder = aryOrder[0]

    # 画图 
    for i in range(0, intNumPoints-1):
        intPt1 = aryActualOrder[i]
        intPt2 = aryActualOrder[i+1]
        plt.plot([aryInput[intPt1][0], aryInput[intPt2][0]], [aryInput[intPt1][1], aryInput[intPt2][1]], 'blue')
        
    # 画头尾相接最后一条线
    plt.plot([aryInput[aryActualOrder[0]][0], aryInput[aryActualOrder[intNumPoints-1]][0]], [aryInput[aryActualOrder[0]][1], aryInput[aryActualOrder[intNumPoints-1]][1]], 'blue')
    plt.show()
