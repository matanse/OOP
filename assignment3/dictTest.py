#!/usr/bin/python

"""
    Usages: 
    ./dictTest.py            (reads out the entire config dict)
    ./dictTest.py wheel air  (sets wheel as key and air as value in the dict)
"""
import sys
import os
from assignment3 import ConfigDict

file_name = 'dict_1.txt'
dict_file = ConfigDict(file_name)

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing "{0} = {1}" to a dict file.'.format(key, value))
    dict_file[key] = value
else:
    if os.path.isfile(file_name):
        line_count = 0
        print('Reading dict file: ')
        with open(file_name) as df:
            # print('        key   value')
            for line in df:
                line_count += 1
                key, value = line.strip().split('=', 1)
                print('        {0} : {1}'.format(key, value))
            if line_count == 0:
                print('       THE FILE IS EMPTY...')
    else:
        print('rrrrrrrrrr')
