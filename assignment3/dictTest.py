#!/usr/bin/python

"""
    Usages: 
    ./dictTest.py            (reads out the entire config dict)
    ./dictTest.py wheel air  (sets wheel as key and air as value in the dict)
"""
import sys
from assignment3 import ConfigDict

dict_file = ConfigDict('dict_1.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('wrote "{0} = {1}" to a dict file.'.format(key, value))
    dict_file[key] = value
else:
    print('Reading dict file: ')
    read_file = open('dict_1.txt', 'r')
    for line in read_file.readlines()[0].split(','):
        dict_line = line.split(':')
        key = dict_line[0]
        value = dict_line[1]
        print(key + value)
        # print('              {0} : {1}'.format(dict_line[0], dict_line[1]))
