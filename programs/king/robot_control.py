import numpy as np
from robot_control_back import *

class PID:
    kp = 0.0 #比例系数
    ki = 0.0 #积分系数
    kd = 0.0 #微分系数
    max_out = 0.0 #最大输出
    max_iout = 0.0 #最大积分输出
    set_value = 0.0 #目标值
    feedback = 0.0 #反馈值
    error = 0.0 #误差值
    last_error = 0.0 #上一次的误差值
    Pout = 0.0 #比例输出
    Iout = 0.0 #积分输出
    Dout = 0.0 #微分输出
    out = 0.0 #总输出
    def __init__(self, kp, ki, kd, max_iout, max_out):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.max_out = max_out
        self.max_iout = max_iout
    
    def pid_calc(self, set_value, feedback):
        '''
        请将这段代码进行完善
        '''
        #将self中的目标值更新
        self.set_value = set_value
        
        #将self中的反馈值更新
        self.feedback = feedback

        #记录两次误差值
        delta_error = self.error - self.last_error

        #将self中的上次误差值更新
        self.last_error = self.error

        #计算当前self中的误差值
        self.error = self.set_value - self.feedback

        #计算当前self中的Pout
        self.Pout = self.kp * self.error

        #计算当前self中的Iout
        self.Iout += self.error * 0.01
        
        #将self中的Iout根据max_iout进行限制
        if (self.Iout < -self.max_iout):
            self.Iout = -self.max_iout
        elif (self.Iout > self.max_iout):
            self.Iout = self.max_iout
        
        #计算self中的Dout，算式中的 0.01 应该与 robot_control_back.py 的 period 值一致
        self.Dout = (delta_error) / 0.01

        #计算self中的out
        self.out = self.Pout + (self.ki * self.Iout) + (self.kd * self.Dout)

        #将self中的out 根据max_out进行限制
        if (self.out < -self.max_out):
            self.out = -self.max_out
        elif (self.out > self.max_out):
            self.out = self.max_out

        return self.out

'''
#请整定参数，分别为比例系数,积分系数,微分系数,最大积分输出,最大输出 
'''
vectory_pid = PID(2.5, 11.8, 1.2, 500, 500)

if __name__ == "__main__":
    #实例化一个机器人速度类
    robot = robot_vectory()
    #第一个参数为PID类， 第二个参数为停止时间
    robot.run(vectory_pid, 20)
