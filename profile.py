from collections import Counter
import sys,time
import print_stdout

CONSOLE_STDOUT = sys.stdout
LOG_STDOUT = open("log.txt","w")
PROFILE_STDOUT = open("profile.txt","w")

class Performance_analysis:
    func_call = Counter()
    func_time = Counter()

    @print_stdout.print_in_profile
    def print_performance(self):
        print('==================== Performance Analysis ====================')
        print('%10s\t%10s\t%10s\t%s' %('time','call','time/call','name'))
        for name in self.func_call:
            print('%10f\t%10d\t%10f\t%s' %(self.func_time[name],self.func_call[name],self.func_time[name]/self.func_call[name],name))


analysis = Performance_analysis()

def profile(func):
    def wrapper(*args,**kwargs):
        function_name = func.__qualname__

        start_time = time.time()
        output = func(*args,**kwargs)
        running_time = time.time() - start_time

        analysis.func_call[function_name] += 1
        analysis.func_time[function_name] += running_time

        return output
    return wrapper




if __name__=="__main__":

    @profile
    def add(x,y):
        return x+y

    @profile
    def add12345(x,y):
        return x+y

    add(1,2)
    for i in range(10):
        print(add12345(i,i))

    analysis.print_performance()