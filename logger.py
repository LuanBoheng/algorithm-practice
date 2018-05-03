from collections import Counter
import sys,time
import print_stdout

CONSOLE_STDOUT = sys.stdout
LOG_STDOUT = open("log.txt","w")
PROFILE_STDOUT = open("profile.txt","w")
LOGGING = False


class Performance_analysis:
    func_call = Counter()
    func_time = Counter()
    runing_log = []

    @print_stdout.print_in_profile
    def print_performance(self):
        print('==================== Performance Analysis ====================')
        print('%10s\t%10s\t%10s\t%s' %('time','call','time/call','name'))
        for name in self.func_call:
            print('%10f\t%10d\t%10f\t%s' %(self.func_time[name],self.func_call[name],self.func_time[name]/self.func_call[name],name))
    
    @print_stdout.print_in_log
    def print_log(self):
        for log in self.runing_log:
            print(*log)

    def print_reports(self):
        self.print_performance()
        if LOGGING:
            self.print_log()

analysis = Performance_analysis()


def logger(func):
    def wrapper(*args,**kwargs):
        func_name = func.__qualname__
        if LOGGING:
            analysis.runing_log.append((func_name,'<',analysis.func_call[func_name],'>','(',*args,kwargs,')'))
      
        start_time = time.time()
        output = func(*args,**kwargs)
        running_time = time.time() - start_time

        if LOGGING:
            analysis.runing_log.append((func_name,'<',analysis.func_call[func_name],'>','(',*args,kwargs,') =', output))
        analysis.func_call[func_name] += 1
        analysis.func_time[func_name] += running_time
        return output
    return wrapper

if __name__=="__main__":
    @logger
    def add(x,y):
        return x+y

    @logger
    def add12345(x,y):
        return add(x,y)

    for i in range(1000):
        print(add12345(i,i))
        for j in range(1000):
            add(j,i)

    analysis.print_performance()
    analysis.print_log()