import debugy,unit_test

test_data = {
    'XXI':21,
    'IV' : 4,
    'XLV':45,
    'XCIX':99,
    'VIII':8,
    'XIV':14
}

def input_format(x): return {'roman':x}

@unit_test.unit_test(test_data,input_format)
@debugy.logger
def solution(roman):
    roman_mum = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    decoded_num = []
    current = roman[0]
    counter = 0

    for c in roman:
        if c == current:
            counter+=1
        else:
            decoded_num.append(roman_mum[current]*counter)
            counter = 1
            current = c
    decoded_num.append(roman_mum[current]*counter)
    
    while len(decoded_num) != 1:
        last_1 = decoded_num[-1]
        last_2 = decoded_num[-2]
        decoded_num = decoded_num[:-1]
        decoded_num[-1] = last_1-last_2 if last_1>last_2 else last_2+last_1
   
    return decoded_num[0]


##best
from functools import reduce
@unit_test.unit_test(test_data,input_format)
@debugy.logger
def solution_best(roman):
    d={'I':1, 'V':5 ,'X':10, 'L':50 ,'C':100, 'D':500,'M':1000}
    
    return reduce(lambda x,y: x+y if x>=y else y-x , (d[c] for c in roman))

debugy.analysis.print_reports()
