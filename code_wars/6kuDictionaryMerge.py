input = ({"A": 1, "B": 2} , {"A": 3})
from collections import defaultdict
def merge(*dicts):
    result = defaultdict(list)
    for d in dicts:
        for k in d:
            result[k] += [d[k]]
    print(result)
    

merge(*input)