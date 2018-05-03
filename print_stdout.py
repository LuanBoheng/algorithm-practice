import sys



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



if __name__ == '__main__':

    @print_in_console
    def print1():
        print(1)

    @print_in_profile
    def print2():
        print(2)

    @print_in_log
    def print3():
        print(3)

    def print4():
        print(4)

    
    print4()
    print2()
    print1()
    print3()
    print4()