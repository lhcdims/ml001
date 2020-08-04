import matplotlib.pyplot as plt
import random as rnd
class robot_vectory:
    first_param =0.1
    second_param = 0.1  
    def run(self, pid, end_time):
        
        run_time_list = []
        run_vectory_list = []
        run_set_value_list = []
        set_value = 1.0
        now_vectory = 0.0
        last_vectory = 0.0
        last_last_vectory = 0.0
        
        run_time = 0.0
        period = 0.01
        a = period**2 / (self.first_param + self.second_param * period + period**2)
        b = (2*self.first_param + self.second_param * period) / (self.first_param + self.second_param * period + period**2)
        c = -self.first_param / (self.first_param + self.second_param * period + period**2)
        while run_time < end_time:
            pid_out = pid.pid_calc(set_value, now_vectory + (rnd.random()-0.5) *0.1)
            last_last_vectory = last_vectory
            last_vectory = now_vectory
            now_vectory = a * pid_out + b * last_vectory + c * last_last_vectory
            
            run_time_list.append(run_time)
            run_vectory_list.append(now_vectory)
            run_set_value_list.append(set_value)
            run_time += period
        
        plt.plot(run_time_list, run_vectory_list)
        plt.plot(run_time_list, run_set_value_list)
        plt.show()
        

