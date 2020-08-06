#!/usr/bin/python

# import sys
# if len(sys.argv) == 3:
#     key = sys.argv[1]
#     value = sys.argv[2]
#     dict = {key: value}
#     new_dict = {}
#     f = open("dict.txt", "a+")
#     print(f)
#     f.write(str(dict))
#     for line in f.readlines():
#         print(line)
#     f.close()

import pickle


class MyClass(object):
    def __init__(self, init_val):
        self.val = init_val

    def increment(self):
        self.val += 1


cc = MyClass(5)
cc.increment()
cc.increment()

with open('datafile.txt', 'w') as fh:
    pickle.dump(cc, fh)
