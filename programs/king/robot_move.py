import numpy as np
import time
from robot_move_back import *
import matplotlib.pyplot as plt
#根据设置的控制指令，计算每个轮子的控制速度(单位rpm， 转每分钟)
#输入的参数 分别为 vx 前进速度 m/s vy 平移速度 m/s wz 旋转速度 wz °/s
#返回的参数 四个轮子的旋转速度 单位 rpm
def control_move_to_me_speed(vx, vy, wz, wheel_radius, robot_lenght, robot_width):
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    #根据机器人运动学公式 进行 麦轮速度解算    需要考虑轮子实际旋转方向, 逆时针为正
    
    #找到最大车轮速度， 如果最大速度大于1000rpm， 需要将所有车轮速度等比例缩小， 使得最大速度为1000rpm
    
    #返回计算出的速度
    return w1,w2,w3,w4


#计算机器人的位置，使用迭代的方式， 
#输入参数 上一次的x坐标，单位 m， 上一次的y坐标 单位m， 上一次的角度， 单位 °, 当前1号车轮速度，单位rpm， 当前2号车轮速度，单位rpm， 
#当前3号车轮速度，单位rpm， 当前4号车轮速度，单位rpm， 定时的周期时间，单位s，车轮的半径， 单位 m， 机器人的长度 单位m， 机器人的宽度，单位m
#返回迭代后的位置 x
def calc_chassis_positon(last_x, last_y, last_angle, w1, w2, w3, w4, period, wheel_radius, robot_lenght, robot_width):
    x = 0.0
    y = 0.0
    angle = 0.0
    #计算这个周期下 在机器人载体坐标系下的 运动距离和 旋转的增量角度
    
    #将机器人载体坐标系的增量距离进行坐标系旋转后，转算成大地坐标系下的增量距离
    
    #将增量距离和上一次距离进行加法
    
    #角度 等于 上一次的角度 加 增量角度
    
    
    return x,y,angle



#根据当前的位置计算设置控制指令， 机器人逆时针旋转
#输入参数x坐标 单位m y坐标 单位m， 机器人当前的朝向角度， 单位 ° 设置旋转半径，单位 m 移动总速度（速度标量限制），单位 m/s ， 在旋转过程中机器人的轴线与半径之间的夹角
#返回参数 机器人前进速度，单位 m/s， 机器人平移速度 m/s， 机器人旋转速度 单位°/s
def robot_move_set_value_according_radius(x, y, angle, radius, speed, angle_bias):
    vx = 0.0
    vy = 0.0
    wz = 0.0
    
    #第一步 可以先调成 机器人不会旋转， 利用麦轮的全向移动进行圆周运动
    #第二步 设置机器人的初始角度后， 在旋转速度后， 验证机器人的圆周运动
    #第三步 机器人边做旋转运动， 边全向移动 以完成 机器人轴线与 半径轴线 重合的功能
    #第四步 考虑机器人的偏移角度 angle_bias, 这时候可以考虑使用角度的闭环控制， 使用简单的P控制即可完成，
    #第五步 加上位置的闭环， 使得机器人不能偏移圆周的半径， 而形成的是螺旋线，而不是圆周运动
    
    
    
    return vx, vy, wz


#发送车轮的控制指令
def send_chassis_set_wheel_speed(robot, w1, w2, w3, w4):
    msg = "chassis wheel w1 " + str(w1) + " w2 " + str(w2) + " w3 " + str(w3) + " w4 " + str(w4) + ';';
    robot.send(msg.encode('utf-8'))

#获取车轮的反馈速度，单位  rpm 转每分钟
def get_chassis_wheel_rpm(robot):
    robot.send("chassis speed ?".encode('utf-8'))
    buf = robot.recv(1024).decode('utf-8')
    buf_split = buf.split()
    w1 = float(buf_split[3])
    w2 = float(buf_split[4])
    w3 = float(buf_split[5])
    w4 = float(buf_split[6])
    return w1, w2, w3, w4
    

x_list = []
y_list = []
angle_list = []
angle_bias_list = []
#if __name__ == "__main__":
start_time = 0.0    #单位 s
end_time = 10       #单位 s
period = 0.02       #单位 s

move_radius = 1        #单位 m
robot_speed = 2     #单位 m/s
angle_bias = 0.6    #单位 弧度

x = move_radius     #单位米
y = 0.0             #单位米
robot_angle = 0.0   #单位 弧度

wheel_radius = 0.05 #车轮半径
robot_lengh = 0.2  #车轮中心 纵向距离
robot_width = 0.2  #车轮中心 横向距离


robot = robot_move.connect(robot_move.AF_INET, robot_move.SOCK_STREAM)

while abs(np.arctan2(y,x) - np.pi) > 0.1 and start_time <  end_time :
    set_vx, set_vy, set_wz = robot_move_set_value_according_radius(x, y, robot_angle, move_radius, robot_speed, angle_bias)
    set_w1, set_w2, set_w3, set_w4 = control_move_to_me_speed(set_vx, set_vy, set_wz, wheel_radius, robot_lengh, robot_width)
    
    send_chassis_set_wheel_speed(robot, set_w1, set_w2, set_w3, set_w4)
    
    w1_rpm, w2_rpm, w3_rpm, w4_rpm = get_chassis_wheel_rpm(robot)
    x,y,robot_angle = calc_chassis_positon(x, y, robot_angle, w1_rpm, w2_rpm, w3_rpm, w4_rpm, period, wheel_radius, robot_lengh, robot_width)
    
    
    x_list.append(x)
    y_list.append(y)
    angle_list.append(robot_angle)
    
    right_angle = np.arctan2(y, x)
    temp_delta_angle = robot_angle - right_angle - angle_bias
    while temp_delta_angle > np.pi:
        temp_delta_angle -= 2*np.pi
    
    while temp_delta_angle < -np.pi:
        temp_delta_angle += 2*np.pi
    angle_bias_list.append(temp_delta_angle)
    
    time.sleep(period)
    start_time+=period

while abs(np.arctan2(y,x)) > 0.1 and start_time <  end_time :
    set_vx, set_vy, set_wz = robot_move_set_value_according_radius(x, y, robot_angle, move_radius, robot_speed, angle_bias)
    set_w1, set_w2, set_w3, set_w4 = control_move_to_me_speed(set_vx, set_vy, set_wz, wheel_radius, robot_lengh, robot_width)
    
    send_chassis_set_wheel_speed(robot, set_w1, set_w2, set_w3, set_w4)
    
    w1_rpm, w2_rpm, w3_rpm, w4_rpm = get_chassis_wheel_rpm(robot)
    x,y,robot_angle = calc_chassis_positon(x, y, robot_angle, w1_rpm, w2_rpm, w3_rpm, w4_rpm, period, wheel_radius, robot_lengh, robot_width)
    
    
    x_list.append(x)
    y_list.append(y)
    time.sleep(period)
    angle_list.append(robot_angle)
    
    
    right_angle = np.arctan2(y, x)
    temp_delta_angle = robot_angle - right_angle - angle_bias
    while temp_delta_angle > np.pi:
        temp_delta_angle -= 2*np.pi
    
    while temp_delta_angle < -np.pi:
        temp_delta_angle += 2*np.pi
    angle_bias_list.append(temp_delta_angle)
    
    start_time+=period

    
robot.shutdown()
plt.plot(x_list,y_list)
plt.show()
plt.plot(angle_list)
plt.show()

plt.plot(angle_bias_list[int(len(angle_bias_list) / 2) : len(angle_bias_list) - 1])
plt.show()
    
    
    
