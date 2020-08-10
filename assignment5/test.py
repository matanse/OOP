#!/usr/bin/python

"""
    Usages: 
    ./dictTest.py            (reads out the entire config dict)
    ./dictTest.py wheel      (gets the value for that key)
    ./dictTest.py wheel air  (sets wheel as key and air as value in the dict)
"""
import sys
import os
from assignment5 import ConfigPickleDict

file_name = './dict_1.txt'
print('before fatching file name')
dict_file = ConfigPickleDict(file_name)
print('after fatching file name')


if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    dict_file[key] = value
    print('wrote "{0} = {1}" to a dict file.'.format(key, value))
elif len(sys.argv) == 2:
    print(sys.argv[1] + ' = ' + dict_file[sys.argv[1]])
else:
    if os.path.isfile(file_name):
        empty = True
        print('Reading dict file: ')
        with open(file_name) as df:
            # print('        key   value')
            for line in df:
                empty = False
                key, value = line.rstrip().lstrip().split('=', 1)
                print('        {0} : {1}'.format(key, value))
            if empty:
                print('       THE FILE IS EMPTY...')
    else:
        print('problem with file existens')
