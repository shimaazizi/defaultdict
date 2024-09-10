class MyDefaultdict:

    """
    A custom defaultdict class that generates default values for missing keys.
    """
    
    def __init__(self, option):
        self.option = option
        self.dic = {}

    def __getitem__(self, item):
        if item not in self.dic:
            self.dic[item] = self.option()
        return self.dic[item]

    def __repr__(self):
        return self.dic.__repr__()

    def __setitem__(self, key, value):
        self.dic[key] = value



# For Test 
if __name__ == '__main__':


    from collections import defaultdict
    
    # For list with collections
    dct = defaultdict(list)
    for i in range(10):
        dct[i].append(i)
    print(dct)
    # with my defaultdict class 
    dct = MyDefaultdict(list)
    for i in range(10):
        dct[i].append(i)
    print(dct)


    # with collections 
    dct = defaultdict(int)
    for i in range(10):
        dct[i] += i
    print(dct)
    # with my defaultdict class 
    dct = MyDefaultdict(int)
    for i in range(10):
        dct[i] += i
    print(dct)