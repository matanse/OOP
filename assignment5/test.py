#!/usr/bin/python

"""
    Usages: 
    ./test.py            (reads out the entire config dict)
    ./test.py wheel      (gets the value for that key)
    ./test.py wheel air  (sets wheel as key and air as value in the dict)
"""
import sys
import os
from assignment5 import WritePickleDictToFile

file_name = './dict_file_1.txt'
dict_file = WritePickleDictToFile(file_name)

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    dict_file[key] = value
    print('wrote "{0} = {1}" to a dict file.'.format(key, value))
elif len(sys.argv) == 2:
    print(str(sys.argv[1]) + ' = ' + str(dict_file[sys.argv[1]]))
else:
    empty_file = True
    print('Reading file: ')
    print('        key   value')
    for key, val in dict_file._file_content.items():
        empty_file = False
        print('          {0} : {1}'.format(key, val))
    if empty_file:
        print(' file is empty')
