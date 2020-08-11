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
dict_file = ConfigPickleDict(file_name)

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    dict_file[key] = value
    print('wrote "{0} = {1}" to a dict file.'.format(key, value))
elif len(sys.argv) == 2:
    print(str(sys.argv[1]) + ' = ' + str(dict_file[sys.argv[1]]))
else:
    if os.path.isfile(file_name):
        empty_file = True
        try:
            print('Reading file: ')
            print('        key   value')
            for key, val in dict_file.items():
                empty_file = False
                print('          {0} : {1}'.format(key, val))
        except:
            print('       THE FILE IS EMPTY...')
            quit()
    else:
        print('problem with file existens')
