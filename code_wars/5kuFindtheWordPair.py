test_data = {

    (('super','bow','bowl','tar','get','book','let'), "superbowl")      :   ['super','bowl',   [0,2]],
    (('bow','crystal','organic','ally','rain','line'), "crystalline")   :   ['crystal','line', [1,5]],
    (('bow','crystal','organic','ally','rain','line'), "rainbow")       :   ['bow','rain',     [4,0]],
    (('bow','crystal','organic','ally','rain','line'), "organically")   :   ['organic','ally', [2,3]],
    (('top','main','tree','ally','fin','line'), "mainline")             :   ['main','line',    [1,5]],
    (('top','main','tree','ally','fin','line'), "treetop")              :   ['top','tree',     [2,0]]

}
def input_format(x): return {'words':x[0],'target':x[1]}

import unit_test
@unit_test.unit_test(test_data,input_format)
def compound_match(words, target):
    d = {}
    for i in range(len(words)):
        if words[i] in target:
            d[words[i]] = i
    result = list(d.items())
    N = len(result)
    for i in range(N):
        for j in range(N):
            if result[i][0]+result[j][0] == target:
                output = [result[i][1],result[j][1]]
    words = map(lambda x:d[x], sorted(output))
    return [words,output]