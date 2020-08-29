import numpy as np

import matplotlib.pyplot as plt
#请完善这部分代码
#判断三点是否在一条直线上， 在一条直线上返回True， 不在一条直线上返回False
def judge_three_point_in_one_line(pos):
    
    
    
    return False

#判断一些点，任意三个点是否在第一条直线上， 存在三点共线返回True， 不在三点共线返回False
def judge_points_in_one_line(pos):
    
    #首先判断 pos的个数是否大于三个，小于3个点情况返回False
    
    #使用三重循环的形式， 一个个遍历所有的点， 
    #开始第一重遍历， 从第一个遍历到倒数第三个点
    
        #开始第二重遍历， 从第一重遍历的下一个点开始遍历 到 倒数第二个点
        
            #开始第三重遍历， 从第二重遍历的下一个点开始遍历 到 倒数第一个点
            
            #取出三重遍历的这三个点， 使用judge_three_point_in_one_line 判断是否共线， 共线的情况 print 共线的点数，并返回 True
            
    
    return False
#计算两点之间的距离
def distance_between_two_point(pos1, pos2):
    #返回 sqrt((x1-x2)**2 + (y1-y2)**2)
    return 0.01

#计算安装顺序排布的点的距离
def distance_points(pos, order):
    
    distance = 0.0
    #使用循环，先从order的第1个点到order的倒数第2个点， 再加上order的倒数第1个点到order的第1个点的距离
    
    #循环到倒数第2个点
        #distance 加上 当前点到order的下一个点的距离， 使用distance_between_two_point计算距离
    
    #distance加上order的最后一个点到order的第一个点的距离
    
    return distance

#获取连接这些点最短距离的排布顺序
def get_pos_order(pos):
    pos_order = [0,1,2]
    #判断点的个数大于2个，即至少3个点
    
    #前三个点构成三角形， 之后一个个点插入，每插入一个点都是寻找使得总距离最小的排序
    
    #从第4点来开始插入，到最后一个点为止
    
        #再开始一个循环，在已有顺序的间隔处都计算一次总距离，保存最小距离的排序
        #声明一个临时最小距离变量并赋值无限大 min_dis = np.inf
        
        #申明一个空的临时顺序列表
        
        #从0开始，到已有点的个数为止
        
            #临时列表复制成当前的顺序列表 pos_order
            
            #在临时列表中插入新加的点
            
            #计算总距离， 使用distance_points
            
            #判断总距离是不是小于临时最小距离变量
            
                #总距离是小于的场合，更新最小距离变量和当前
        
        #小循环结束，新加入的点找到对应最小距离的顺序
        
    
    #大循环结束，返回最后的顺序
    return pos_order

if __name__ == "__main__":
    '''
    使用3个'可以进行区块注释，可以将下面的注释去除进行单个函数测试
    '''
    
    point_pos = []
    while True:
        pos = input("输入点坐标（形如0,0）或者Q退出：")
        if pos.upper() == 'Q':
            if len(point_pos) > 2:
                if judge_points_in_one_line(point_pos):
                    print("请重新输入")
                    point_pos = []
                    continue
                else:
                    break
            else:
                print("输入的点数小于3个，请重新输入")
                point_pos = []
                continue
        #转化点的坐标到列表中        
        temp = pos.split(',')
        temp_positon = []
        temp_positon.append(float(temp[0]))
        temp_positon.append(float(temp[1]))
        point_pos.append(temp_positon)
    
    #连接这些点的顺序
    point_order = get_pos_order(point_pos)
    
    #将连接的情况回执出来
    i = 0
    while i < len(point_order)-1:
        x = []
        y = []
        x.append(point_pos[point_order[i]][0])
        x.append(point_pos[point_order[i+1]][0])
        y.append(point_pos[point_order[i]][1])
        y.append(point_pos[point_order[i+1]][1])
        plt.plot(x,y)
        i+=1
    
    x = []
    y = []
    x.append(point_pos[point_order[0]][0])
    x.append(point_pos[point_order[i]][0])
    y.append(point_pos[point_order[0]][1])
    y.append(point_pos[point_order[i]][1])
    plt.plot(x,y)
    plt.show()
    
    
    
    '''
    test_pos=[[0,0],[1,1],[2,2]]
    #输出 True
    print(judge_three_point_in_one_line(test_pos))
    test_pos=[[0,0],[1,1],[3,2]]
    #输出 False
    print(judge_three_point_in_one_line(test_pos))
    '''
    
    '''
    test_pos=[[0,0],[1,1],[2,3],[2,2]]
    #输出 True
    print(judge_points_in_one_line(test_pos))
    test_pos=[[0,0],[1,1],[2,3],[2,5]]
    #输出 False
    print(judge_points_in_one_line(test_pos))
    '''
    
    '''
    pos1 = [0,0]
    pos2 = [1,0]
    #输出 1.0
    print(distance_between_two_point(pos1, pos2))
    '''
    
    '''
    test_pos=[[0,0],[0,1],[1,1],[1,0]]
    test_order = [0, 1, 2, 3]
    #输出 4.0
    print(distance_points(test_pos, test_order))
    '''
    
    '''
    test_pos=[[0,0],[0,1],[1,0],[1,1]]
    #输出 [0, 1, 3, 2]
    print(get_pos_order(test_pos))
    '''
    
    