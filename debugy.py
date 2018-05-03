import time,sys
from collections import Counter

log_file_name = "log.txt"
file_stdout = open(log_file_name,"w")
old_stdout = sys.stdout

def print_in_file(func):
    def wrapper(*args,**kwargs):
        sys.stdout = file_stdout
        output = func(*args,**kwargs)
        sys.stdout = old_stdout
        return output
    return wrapper

def print_in_console(func):
    def wrapper(*args,**kwargs):
        sys.stdout = old_stdout
        output = func(*args,**kwargs)
        sys.stdout = file_stdout
        return output
    return wrapper

class Debug:
    
    def __init__(self):
        
        self.function_call_log = []
        self.func_call = Counter()
        self.func_time = Counter()

    @print_in_file
    def print_full_log(self):
        print('========================== Full Log ==========================')
        print('%10s\t%s' %('time','info',))
        for log in self.function_call_log:
            print('%10f\t%s' %(log['running_time'],log['info']))

    def print_performance_analysis(self):
        print('==================== Performance Analysis ====================')
        print('%10s\t%10s\t%10s\t%s' %('time','call','time/call','name'))
        for name in self.func_call:
            print('%10f\t%10d\t%10f\t%s' %(self.func_time[name],self.func_call[name],self.func_time[name]/self.func_call[name],name))

    @print_in_file
    def print_report(self):  
        self.print_performance_analysis()
        self.print_full_log()

debug_report = Debug()


def debug(func):
    def wrapper(*args,**kwargs):
        function_name = func.__qualname__
        print_statement = function_name+'('
        for arg in args: 
            print_statement += str(arg)+','
        dict_args = {**kwargs}
        for arg in dict_args:
            print_statement += str(arg)+':'+str(dict_args[arg])+','
        print_statement = print_statement[:-1] + ')'
        
        start_time = time.time()
    
        try:
            output = func(*args,**kwargs)
        except:
            debug_report.function_call_log.append({'function_name':function_name,'running_time':-1,'info':print_statement})
            print('==================== Performance Analysis ==========')
            debug_report.print_performance_analysis()
            print('==================== Last Statement ================')
            # print_full_log()
            print(print_statement)
            print('====================================================')
            output = func(*args,**kwargs)
        
        running_time = time.time() - start_time
        print_statement += ' = '+str(output)

        debug_report.func_call[function_name] += 1
        debug_report.func_time[function_name] += running_time

        debug_report.function_call_log.append({'function_name':function_name,'running_time':running_time,'info':print_statement})

        return output
    return wrapper


@debug
def add(x,y):
    return x+y

@debug
def add12345(x,y):
    return x+y

if __name__=="__main__":
    add(1,2)
    add(1,'e')
    for i in range(10):
        print(add12345(i,i))
    debug_report.print_report()