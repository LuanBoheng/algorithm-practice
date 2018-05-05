from collections import Counter
import sys,time

class STDOUT:
    def __init__(self):
        self.CONSOLE = sys.stdout
        self.LOG = open("log.txt","w")
        self.PROFILE = open("profile.txt","w")

stdout = STDOUT()

def print_in_std(target_stdout,func):
    def wrapper(*args,**kwargs):
        old_stdout = sys.stdout
        sys.stdout = target_stdout
        output = func(*args,**kwargs)
        sys.stdout = old_stdout
        return output
    return wrapper

def print_in_console(func):
    return print_in_std(stdout.CONSOLE,func)

def print_in_log(func):
    return print_in_std(stdout.LOG,func)

def print_in_profile(func):
    return print_in_std(stdout.PROFILE,func)

class Performance_analysis:

    def __init__(self):
        self.func_call = Counter()
        self.func_time = Counter()
        self.runing_log = []
        self.LOGGING = True
    

    @print_in_profile
    def print_performance(self):
        print('==================== Performance Analysis ====================')
        print('%10s\t%10s\t%10s\t%s' %('time','call','time/call','name'))
        for name in self.func_call:
            print('%10f\t%10d\t%10f\t%s' %(self.func_time[name],self.func_call[name],self.func_time[name]/self.func_call[name],name))
    
    @print_in_log
    def print_log(self):
        for log in self.runing_log:
            print(*log)

    def print_reports(self):
        self.print_performance()
        if self.LOGGING:
            self.print_log()

analysis = Performance_analysis()


def logger(func):
    def wrapper(*args,**kwargs):
        func_name = func.__qualname__
        if analysis.LOGGING:
            analysis.runing_log.append((func_name,'<',analysis.func_call[func_name],'>','(',*args,kwargs,')'))
      
        start_time = time.time()
        output = func(*args,**kwargs)
        running_time = time.time() - start_time

        if analysis.LOGGING:
            analysis.runing_log.append((func_name,'<',analysis.func_call[func_name],'>','(',*args,kwargs,') =', output))
        analysis.func_call[func_name] += 1
        analysis.func_time[func_name] += running_time
        return output
    return wrapper

if __name__=="__main__":
    analysis.LOGGING = True

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

    analysis.print_reports()