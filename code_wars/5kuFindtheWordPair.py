test_data = {

    (('super','bow','bowl','tar','get','book','let'), "superbowl")      :   ['super','bowl',   [0,2]],
    (('bow','crystal','organic','ally','rain','line'), "crystalline")   :   ['crystal','line', [1,5]],
    (('bow','crystal','organic','ally','rain','line'), "rainbow")       :   ['bow','rain',     [4,0]],
    (('bow','crystal','organic','ally','rain','line'), "organically")   :   ['organic','ally', [2,3]],
    (('top','main','tree','ally','fin','line'), "mainline")             :   ['main','line',    [1,5]],
    (('top','main','tree','ally','fin','line'), "treetop")              :   ['top','tree',     [2,0]]

}
def input_format(x): return {'words':x[0],'target':x[1]}

import unit_test,debugy

@unit_test.unit_test(test_data,input_format)
@debugy.logger
def compound_match(words, target):
    d = {}
    for i in range(len(words)):
        if words[i] in target:
            if words[i] not in d:
                d[words[i]] = i
    result = list(d.items())
    N = len(result)
    for i in range(N):
        for j in range(N):
            if result[i][0]+result[j][0] == target:
                output = [result[i][1],result[j][1]]
                words = list(map(lambda x:words[x], sorted(output)))
                return [*words,output]

@unit_test.unit_test(test_data,input_format)
@debugy.logger
def compound_match_best(words, target):
    for i in range(1,len(target)-1):
        t1 = target[:i]; t2 = target[i:]
        if (t1 in words) and (t2 in words):
            i1 = words.index(t1); i2 = words.index(t2)
            return  ([t1, t2] if i1<i2 else [t2, t1]) + [[i1,i2]]

debugy.analysis.print_reports()