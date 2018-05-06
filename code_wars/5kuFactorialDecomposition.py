import unit_test,debugy


test_data ={
    12:"2^10 * 3^5 * 5^2 * 7 * 11",
    22:"2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19",
    25:"2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23",
    5000:'',
    10000:'',
    5000:''
}

import math, collections
@debugy.logger
def is_prime1(n):
    for i in range(2,math.floor(n**0.5)+1): 
        if n%i == 0: return False
    return True
@debugy.logger
def resolve_prime1(n):
    result = collections.Counter()
    for i in range(2,math.floor(n**0.5)+1):
        while is_prime1(i) and n%i==0:
            result[i] += 1
            n/=i
    result[n]+= 1
    return result

@debugy.logger
def decomp_real1(n):
    result = collections.Counter()
    for i in range(2,n+1):
        prime_counter = resolve_prime1(i)
        result += prime_counter
    return result

@unit_test.unit_test(test_data,lambda x:{'n':x})
@debugy.logger
def decomp1(n):
    output = ''
    result = decomp_real1(n)
    if 1 in result: result.pop(1)
    for k in sorted(list(result.keys())):
        if result[k]>1:
            output += str(k)+'^'+str(result[k])+' * '
        else:
            output += str(k)+' * '
    return output[:-3]
#########################################################

resolved_prime = {}
resolved_decomp = {}

@debugy.logger
def is_prime(n):
    if n in resolved_prime: return len(resolved_prime[n]) == 1
    else:
        for i in range(2,math.floor(n**0.5)+1): 
            if n%i == 0: return False
        return True

@debugy.logger
def resolve_prime(n):
    if n in resolved_prime: return resolved_prime[n]
    else:
        result = collections.Counter()
        for i in range(2,math.floor(n**0.5)+1):
            while is_prime(i) and n%i==0:
                result[i] += 1
                n/=i
        result[n]+= 1
        return result

@debugy.logger
def decomp_real(n):
    if n in resolved_decomp: return resolved_decomp[n]
    else:
        result = collections.Counter()
        for i in range(2,n+1):
            if n in resolved_prime: prime_counter = resolved_prime[i]
            else:
                prime_counter = resolve_prime(i)
                resolved_prime[i] = prime_counter
            result += prime_counter
        resolved_decomp[n] = result
        return result

@unit_test.unit_test(test_data,lambda x:{'n':x})
@debugy.logger
def decomp(n):
    output = ''
    result = decomp_real(n)
    if 1 in result: result.pop(1)
    for k in sorted(list(result.keys())):
        if result[k]>1:
            output += str(k)+'^'+str(result[k])+' * '
        else:
            output += str(k)+' * '
    return output[:-3]

debugy.analysis.print_reports()



