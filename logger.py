import print_stdout


func_list = dict()

@print_stdout.print_in_console
def func_wrapper(func):
    return func


def logger(func):
    @print_stdout.print_in_log
    def wrapper(*args,**kwargs):
        func_name = func.__qualname__
        if func_name not in func_list:
            func_list[func_name] = len(func_list)
        print(func_list[func_name]*'\t',func_name,'(',*args,kwargs,') start')
        output = func_wrapper(func)(*args,**kwargs)
        print(func_list[func_name]*'\t',func_name,'(',*args,kwargs,') =', output)
        return output
    return wrapper




if __name__=="__main__":
    @logger
    def add(x,y):
        return x+y

    @logger
    def add12345(x,y):
        return add(x,y)

    for i in range(10):
        print(add12345(i,i))
        for j in range(10):
            add(j,i)
