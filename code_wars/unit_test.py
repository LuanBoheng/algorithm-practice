def unit_test(test_data,input_format):
    def warpper(func):
        print('==================',func.__qualname__,'==================')
        for test in test_data:
            result = func(**input_format(test))
            print (test_data[test]==result,'(',test,')','->',result,'(',test_data[test],')')
    return warpper
            