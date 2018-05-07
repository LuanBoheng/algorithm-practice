from collections import defaultdict,Counter
import debugy

class Cache:
    current_func = None
    cache_storage = defaultdict(dict)
    
c = Cache()

def wrapper(*args,**kwargs):
        key = (str(args),str(kwargs))
        if key in c.cache_storage[c.current_func]:
            return c.cache_storage[c.current_func][key]
        else:
            result = c.current_func(*args,**kwargs)
            c.cache_storage[c.current_func][key] = result
            return result

def cache(func):
    c.current_func = func
    wrapper.__qualname__ = func.__qualname__
    return wrapper

if __name__ == '__main__':

    @debugy.logger
    def feb(n):
        if n == 0 or n == 1: return 1
        else: return feb(n-1) + feb(n-2)
    
    @debugy.logger
    @cache
    def feb_cache(n):
        if n == 0 or n == 1: return 1
        else: return feb_cache(n-1) + feb_cache(n-2)

    for i in range(25):
        print(i,feb(i))
    
    for i in range(25):
        print(i,feb_cache(i))
    
    debugy.analysis.print_reports()