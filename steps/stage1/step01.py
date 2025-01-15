class Variable:
    def __init__(self, data):
        self.data = data

import numpy as np

def test():
    data = np.array(1.0)
    x = Variable(data=data)
    print(x.data)

if __name__ == '__main__':
    test()