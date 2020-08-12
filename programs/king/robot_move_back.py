import numpy as np
import _thread
import time
import random as rnd

def robot_run(robot, delay):
    while True:
        if robot.quit_flag == 1:
            break
        
        time.sleep(delay)
        i = 0
        while i < 4:
            robot.last_last_vectory[i] = robot.last_vectory[i]
            robot.last_vectory[i] = robot.w_rpm[i]
            robot.w_rpm[i] = robot.a * robot.set_w_rpm[i] + robot.b * robot.last_vectory[i] + robot.c * robot.last_last_vectory[i]
            i+=1
        
    
class robot_move:
    AF_INET = 1
    SOCK_STREAM = 1
    
    quit_flag = 0
    reply_speed_flag = 0
    set_w_rpm = [0.0, 0.0, 0.0, 0.0]
    w_rpm = [0.0, 0.0, 0.0, 0.0]
    
    error_rpm = 0
    
    first_param =0.0
    second_param = 0.001  
    
    period = 0.01
    
    last_vectory = [0.0, 0.0, 0.0, 0.0]
    last_last_vectory = [0.0, 0.0, 0.0, 0.0]
    a = 0.0
    b = 0.0
    c = 0.0
    def connect(temp1, temp2):
        
        robot = robot_move()
        robot.a = robot.period**2 / (robot.first_param + robot.second_param * robot.period + robot.period**2)
        robot.b = (2*robot.first_param + robot.second_param * robot.period) / (robot.first_param + robot.second_param * robot.period + robot.period**2)
        robot.c = -robot.first_param / (robot.first_param + robot.second_param * robot.period + robot.period**2)
        
        robot.quit_flag = 0
        # 创建两个线程
        try:
           _thread.start_new_thread(robot_run , (robot, 0.01) )
        except:
           print ("Error: 无法启动线程")
        
        return robot
        
    def shutdown(self):
        self.quit_flag = 1
        
        print("w1:" + str(self.w_rpm[0]) + ',w2:' + str(self.w_rpm[1]) + ',w3:' + str(self.w_rpm[2]) + ',w4:' + str(self.w_rpm[3]))
        return 1
    def recv(self, time):
        if self.reply_speed_flag != 1:
            return
        msg = ("0 0 0 " + str(self.w_rpm[0] + (rnd.random() - 0.5) * self.error_rpm) + " "  + str(self.w_rpm[1] + (rnd.random() - 0.5) * self.error_rpm) + " " + " "  + str(self.w_rpm[2] + (rnd.random() - 0.5) * self.error_rpm) + " "  + str(self.w_rpm[3] + (rnd.random() - 0.5) * self.error_rpm))
        return msg.encode('utf-8')
        
    def send(self, msg):
        message = msg.decode('utf-8')
        msg_split = message.split(' ')
        if msg_split[2] == '?':
            self.reply_speed_flag = 1
        
        i = 2
        while i < len(msg_split):
            if msg_split[i][0] == 'w':
                if msg_split[i][1] > '0' and msg_split[i][1] < '5':
                    self.set_w_rpm[ int(msg_split[i][1],10) - 1 ] = float(msg_split[i+1].split(';')[0])
                    i+=2
                    continue
            i+=1
        
        
        return True


if __name__ == "__main__":
    robot = robot_move.connect(robot_move.AF_INET, robot_move.SOCK_STREAM)
    robot.send("chassis wheel w1 100 w2 2 w3 3.2 w4 1.2;".encode('utf-8'))
    i = 0
    while i < 10:
        robot.send("chassis speed ?".encode('utf-8'))
        print(robot.recv(1024).decode('utf-8'))
        time.sleep(1)
        i+=1
    
        
    robot.shutdown()
